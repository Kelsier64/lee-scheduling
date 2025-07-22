from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
from typing import List, Optional
import uvicorn

app = FastAPI()

# Pydantic models

class Person(BaseModel):
    name: str
    work: str
    days: List[str]
    times: int
    work_times: int = 0

class People(BaseModel):
    people: List[Person]

class ScheduleRequest(BaseModel):
    year: int
    month: int
    people: List[Person]

class Department(BaseModel):
    internal: str = ""
    surgical: str = ""
    an: str = ""
    noon: str = ""

class NightDepartment(BaseModel):
    internal: str = ""
    surgical: str = ""
    an: str = ""
    stay: str = ""

class Day(BaseModel):
    date: str
    day: Department
    night: NightDepartment

class ScheduleResponse(BaseModel):
    success: bool
    message: str
    schedule: List[Day]
    summary: List[dict]
    statistics: dict

# Scheduling functions from main.py
def create_schedule(year, month):
    """創建指定年月的排班表"""
    month = []
    
    first_day = datetime.datetime(year, month, 1)
    
    if month == 12:
        next_month = datetime.datetime(year + 1, 1, 1)
    else:
        next_month = datetime.datetime(year, month + 1, 1)

    num_days = (next_month - first_day).days
    
    for i in range(num_days):
        current_date = first_day + datetime.timedelta(days=i)
        day_of_week = current_date.weekday()
        noon_value = "X" if day_of_week in [1, 2, 3] else ""
        
        new_day = {
            "date": current_date.strftime("%Y-%m-%d"),
            "day": {
                "internal": "",
                "surgical": "",
                "an": "",
                "noon": noon_value
            },
            "night": {
                "internal": "",
                "surgical": "",
                "an": "",
                "stay": ""
            }
        }
        month.append(new_day)
    
    return month

def can_work_shift(person, day_index, shift):
    """檢查人員是否可以上指定班次"""
    availability = person["days"][day_index]
    
    if shift == "day":
        return availability in ["ok", "no_night", "work-no_night"]
    elif shift == "night":
        return availability in ["ok", "no_day"]
    return False

def get_available_people_for_slot(day_index, shift, department, assigned_today, people, schedule):
    """獲取可分配到指定班次的人員列表，按優先級排序"""
    available_people = []
    
    for person in people:
        if (person["work_times"] < person["times"] and 
            person["name"] not in assigned_today and
            can_work_shift(person, day_index, shift)):
            
            priority = 0
            
            if department == "internal" and person["work"] == "internal":
                priority += 100
            elif department == "surgical" and person["work"] == "surgical":
                priority += 100
            elif department == "an" and person["work"] == "an":
                priority += 100
            elif person["work"] == "ok":
                priority += 50
            
            remaining_shifts = person["times"] - person["work_times"]
            priority += remaining_shifts * 10
            
            remaining_days = len(schedule) - day_index
            available_remaining_days = 0
            for future_day in range(day_index, len(schedule)):
                if person["days"][future_day] != "OFF":
                    available_remaining_days += 1
            
            if available_remaining_days > 0:
                scarcity_factor = remaining_shifts / available_remaining_days
                priority += scarcity_factor * 20
            
            month_end_factor = (day_index / len(schedule)) * remaining_shifts * 5
            priority += month_end_factor
            
            available_people.append((person, priority))
    
    available_people.sort(key=lambda x: x[1], reverse=True)
    return [person for person, _ in available_people]

def get_all_slots(schedule):
    """獲取所有需要分配的班次位置"""
    slots = []
    for day_index, day in enumerate(schedule):
        date = day["date"]
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        day_of_week = current_date.weekday()
        
        all_shifts = [
            ("day", "internal"), ("day", "surgical"), ("day", "an"), ("day", "noon"),
            ("night", "internal"), ("night", "surgical"), ("night", "an"), ("night", "stay")
        ]
        
        for shift, department in all_shifts:
            if department == 'noon' and day_of_week in [1, 2, 3]:
                continue
            slots.append((day_index, shift, department))
    
    return slots

def calculate_slot_difficulty(day_index, shift, department):
    """計算班次的難度分數（分數越高越難填補）"""
    difficulty = 0
    
    if shift == "night":
        difficulty += 10
    
    if department in ["internal", "surgical", "an"]:
        difficulty += 5
    
    difficulty += day_index * 0.1
    
    return difficulty

def assign_schedule_backtrack(people, schedule):
    """使用回溯法進行最優排班分配"""
    
    for person in people:
        person["work_times"] = 0
    
    for day in schedule:
        for shift in ["day", "night"]:
            for dept in day[shift]:
                if day[shift][dept] != "X":
                    day[shift][dept] = ""
    
    slots = get_all_slots(schedule)
    slots.sort(key=lambda x: calculate_slot_difficulty(x[0], x[1], x[2]), reverse=True)
    
    def backtrack(slot_index):
        if slot_index == len(slots):
            return True
        
        day_index, shift, department = slots[slot_index]
        
        assigned_today = set()
        for s in ["day", "night"]:
            for d in schedule[day_index][s]:
                if schedule[day_index][s][d] and schedule[day_index][s][d] != "X":
                    assigned_today.add(schedule[day_index][s][d])
        
        available_people = get_available_people_for_slot(day_index, shift, department, assigned_today, people, schedule)
        
        for person in available_people:
            schedule[day_index][shift][department] = person["name"]
            person["work_times"] += 1
            
            if backtrack(slot_index + 1):
                return True
            
            schedule[day_index][shift][department] = ""
            person["work_times"] -= 1
        
        return False
    
    success = backtrack(0)
    return success

def assign_schedule_hybrid(people, schedule):
    """使用混合策略：先用貪婪演算法，失敗後用回溯法"""
    
    for person in people:
        person["work_times"] = 0
    
    for day in schedule:
        for shift in ["day", "night"]:
            for dept in day[shift]:
                if day[shift][dept] != "X":
                    day[shift][dept] = ""
    
    shift_priority = [
        ("night", "internal"), ("night", "surgical"), ("night", "an"),
        ("day", "internal"), ("day", "surgical"), ("day", "an"),
        ("night", "stay"), ("day", "noon")
    ]
    
    for day_index, day in enumerate(schedule):
        assigned_today = set()
        
        for shift, department in shift_priority:
            if department == 'noon' and day[shift][department] == 'X':
                continue
            
            if day[shift][department] != "":
                continue
            
            available_people = get_available_people_for_slot(day_index, shift, department, assigned_today, people, schedule)
            
            if available_people:
                selected_person = available_people[0]
                day[shift][department] = selected_person["name"]
                selected_person["work_times"] += 1
                assigned_today.add(selected_person["name"])
    
    empty_count, total_shifts, empty_details = count_empty_shifts(schedule)
    
    if empty_count == 0:
        return True
    else:
        success = assign_schedule_backtrack(people, schedule)
        return success

def assign_schedule(people, schedule):
    """主排班函數"""
    return assign_schedule_hybrid(people, schedule)

def count_empty_shifts(schedule):
    """統計空班數量"""
    empty_count = 0
    total_shifts = 0
    empty_details = []
    
    for i, day in enumerate(schedule):
        date = day["date"]
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        day_of_week = current_date.weekday()
        
        shifts_to_check = [
            ("day", "internal", "日班內科"),
            ("day", "surgical", "日班外科"),
            ("day", "an", "日班安康"),
            ("day", "noon", "中午班"),
            ("night", "internal", "夜班內科"),
            ("night", "surgical", "夜班外科"),
            ("night", "an", "夜班安康"),
            ("night", "stay", "留守班")
        ]
        
        for shift, department, shift_name in shifts_to_check:
            if department == 'noon' and day_of_week in [1, 2, 3]:
                continue
                
            total_shifts += 1
            if day[shift][department] == "":
                empty_count += 1
                empty_details.append(f"第{i+1}天 ({date}) - {shift_name}")
    
    return empty_count, total_shifts, empty_details

def convert_pydantic_to_dict(people_list: List[Person]) -> List[dict]:
    """Convert Pydantic Person objects to dict format expected by scheduling functions"""
    return [
        {
            "name": person.name,
            "work": person.work,
            "days": person.days,
            "times": person.times,
            "work_times": person.work_times
        }
        for person in people_list
    ]

@app.post("/schedule", response_model=ScheduleResponse)
async def schedule(request: ScheduleRequest):
    try:
        # Convert Pydantic objects to dict format
        people_dict = convert_pydantic_to_dict(request.people)
        
        # Create the schedule structure
        schedule = create_schedule(request.year,request.month)

        # Run the scheduling algorithm
        success = assign_schedule(people_dict, schedule)
        
        # Calculate statistics
        empty_count, total_shifts, empty_details = count_empty_shifts(schedule)
        coverage_rate = (total_shifts - empty_count) / total_shifts * 100 if total_shifts > 0 else 0
        
        # Create summary
        summary = [
            {
                "name": person["name"],
                "assigned": person["work_times"],
                "required": person["times"]
            }
            for person in people_dict
        ]
        
        # Convert schedule to response format
        response_schedule = []
        for day_data in schedule:
            day_obj = Day(
                date=day_data["date"],
                day=Department(**day_data["day"]),
                night=NightDepartment(**day_data["night"])
            )
            response_schedule.append(day_obj)
        
        message = "排班成功完成！" if success else f"排班完成，但有 {empty_count} 個空班"
        
        return ScheduleResponse(
            success=success,
            message=message,
            schedule=response_schedule,
            summary=summary,
            statistics={
                "total_shifts": total_shifts,
                "assigned_shifts": total_shifts - empty_count,
                "empty_shifts": empty_count,
                "coverage_rate": round(coverage_rate, 1),
                "empty_details": empty_details
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"排班過程中發生錯誤: {str(e)}")

@app.get("/")
async def root():
    return {"message": "員工排班系統 API", "version": "1.0.0"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

