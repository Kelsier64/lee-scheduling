import datetime

def create_month(year, month_num):
    """創建指定年月的排班表
    
    Args:
        year: 年份
        month_num: 月份
    
    Returns:
        month: 包含整個月每一天的排班結構
    """
    month = []
    
    # 創建一天的模板結構
    day_template = {
        "date": "",  # 日期
        "day": {"internal": "", "surgical": "", "an": "", "noon": ""},  
        "night": {"internal": "", "surgical": "", "an": "", "stay": ""}  
    }
    
    # 獲取指定月份的第一天
    first_day = datetime.datetime(year, month_num, 1)
    
    # 計算該月份的總天數
    if month_num == 12:
        next_month = datetime.datetime(year + 1, 1, 1)
    else:
        next_month = datetime.datetime(year, month_num + 1, 1)
    
    num_days = (next_month - first_day).days
    
    # 為整個月的每一天創建排班結構
    for i in range(num_days):
        # 計算當前日期
        current_date = first_day + datetime.timedelta(days=i)
        
        # 獲取星期幾 (0=週一, 1=週二, 2=週三, 3=週四, 等等)
        day_of_week = current_date.weekday()
        
        # 週二(1)、週三(2)、週四(3)的中午班設為"X"
        noon_value = "X" if day_of_week in [1, 2, 3] else ""
        
        # 複製模板創建新的一天
        new_day = {
            "date": current_date.strftime("%Y-%m-%d"),
            "day": {
                "internal": "",    # 內科日班
                "surgical": "",    # 外科日班
                "an": "",         
                "noon": noon_value # 中午班
            },
            "night": {
                "internal": "",   # 內科夜班
                "surgical": "",   # 外科夜班
                "an": "",        
                "stay": ""       # 留守夜班
            }
        }
        month.append(new_day)
    
    return month

# 使用範例：
current_year = datetime.datetime.now().year
schedule = create_month(current_year, 7)  # 創建7月份的排班表


# 定義所有工作人員的基本信息和可用性
jian = {    
"name": "Jian",        # 姓名
"work":"internal",     # 工作類型：內科
"days": ["no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","OFF","OFF","OFF","OFF","OFF","OFF","OFF","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night",],
# 每天的可用性：no_night=不能上夜班, OFF=休息, ok=可上任何班, no_day=不能上日班, work-no_night=工作但不上夜班
"times":14,            # 本月需要上班的總次數
"work_times":0         # 目前已分配的班次數
}
feng = {
"name": "Feng",        # 姓名
"work":"ok",          # 工作類型：靈活（可分配到任何科別）
"days":["ok","ok","OFF","ok","ok","ok","ok","OFF","ok","ok","OFF","OFF","OFF","ok","OFF","ok","ok","OFF","ok","OFF","ok","ok","ok","OFF","ok","ok","OFF","ok","ok","ok","ok",],
"times":10,           # 本月需要上班的總次數
"work_times":0        # 目前已分配的班次數
}
ming = {
"name": "Ming",        # 姓名
"work":"internal",     # 工作類型：內科
"days": ["ok","ok","ok","ok","OFF","ok","ok","OFF","ok","ok","ok","ok","OFF","ok","no_day","ok","no_day","ok","ok","ok","ok","no_day","ok","ok","ok","ok","ok","ok","no_day","ok","no_day"],
"times":16,           # 本月需要上班的總次數
"work_times":0        # 目前已分配的班次數
}
lan = {
"name": "Lan",         # 姓名
"work":"internal",     # 工作類型：內科
"days": ['no_night', 'work-no_night', 'no_night', 'work-no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'work-no_night', 'no_night', 'no_night', 'work-no_night', 'work-no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'work-no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'work-no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'work-no_night',"no_night"],
"times":8,            # 本月需要上班的總次數
"work_times":0        # 目前已分配的班次數
}
mou = {
"name": "Mou",         # 姓名
"work":"an",         
"days": ['no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night'],
"times":13,           # 本月需要上班的總次數
"work_times":0        # 目前已分配的班次數
}
teng ={
"name": "Teng",
"work":"ok",
"days": ['no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night'],
"times":16,
"work_times":0
}
zhi = {
"name": "Zhi",
"work":"ok",
"days":['OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok'],
"times":15,
"work_times":0
}        
hua ={
"name": "Hua",
"work":"ok",
"days":['ok', 'ok', 'OFF', 'no_day', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'no_day', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'],
"times":15,
"work_times":0
}
da = {
"name": "Da",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF'],
"times":16,
"work_times":0
}
jin = {
"name": "Jin",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'no_night', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'no_day', 'ok', 'ok', 'ok', 'ok', 'ok'],
"times":8,
"work_times":0
}
yong ={
"name": "Yong",
"work":"ok",    
"days":['OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok'],
"times":16,
"work_times":0
}
yi = {
"name": "Yi",
"work":"ok",
"days":['OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok'],
"times":15,
"work_times":0
}
fang = {
"name": "Fang",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'no_night', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF'],
"times":15,
"work_times":0
}
han = {
"name": "Han",
"work":"ok",
"days":['OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok'],
"times":14,
"work_times":0
}
chun = {
"name": "Chun",        # 姓名
"work":"surgical",     # 工作類型：外科
"days":['no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night'],
"times":13,           # 本月需要上班的總次數
"work_times":0        # 目前已分配的班次數
}
jian4 = {
"name": "Jian4",
"work":"ok",  
"days":['ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok'],
"times":15,
"work_times":0
}
qiang = {
"name": "Qiang",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok'],
"times":14,
"work_times":0
}


# 所有工作人員列表
people = [jian, feng, ming, lan, mou, teng, zhi, hua, da, jin, yong, yi, fang, han, chun, jian4, qiang]

def can_work_shift(person, day_index, shift):
    """檢查人員是否可以上指定班次"""
    availability = person["days"][day_index]
    
    if shift == "day":
        return availability in ["ok", "no_night", "work-no_night"]
    elif shift == "night":
        return availability in ["ok", "no_day"]
    return False

def get_available_people_for_slot(day_index, shift, department, assigned_today):
    """獲取可分配到指定班次的人員列表，按優先級排序"""
    available_people = []
    
    for person in people:
        if (person["work_times"] < person["times"] and 
            person["name"] not in assigned_today and
            can_work_shift(person, day_index, shift)):
            
            # 計算優先級分數（分數越高優先級越高）
            priority = 0
            
            # 專科匹配優先
            if department == "internal" and person["work"] == "internal":
                priority += 100
            elif department == "surgical" and person["work"] == "surgical":
                priority += 100
            elif department == "an" and person["work"] == "an":
                priority += 100
            elif person["work"] == "ok":
                priority += 50
            
            # 剩餘班次數較多的人優先
            remaining_shifts = person["times"] - person["work_times"]
            priority += remaining_shifts * 10
            
            # 計算該人員在剩餘天數中的可用天數
            remaining_days = len(schedule) - day_index
            available_remaining_days = 0
            for future_day in range(day_index, len(schedule)):
                if person["days"][future_day] != "OFF":
                    available_remaining_days += 1
            
            # 如果這個人員後面可用天數很少，優先使用
            if available_remaining_days > 0:
                scarcity_factor = remaining_shifts / available_remaining_days
                priority += scarcity_factor * 20
            
            # 月底加權：越到月底，優先使用剩餘班次多的人
            month_end_factor = (day_index / len(schedule)) * remaining_shifts * 5
            priority += month_end_factor
            
            available_people.append((person, priority))
    
    # 按優先級排序（高分優先）
    available_people.sort(key=lambda x: x[1], reverse=True)
    return [person for person, _ in available_people]

def get_all_slots():
    """獲取所有需要分配的班次位置"""
    slots = []
    for day_index, day in enumerate(schedule):
        date = day["date"]
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        day_of_week = current_date.weekday()
        
        # 定義所有班次
        all_shifts = [
            ("day", "internal"), ("day", "surgical"), ("day", "an"), ("day", "noon"),
            ("night", "internal"), ("night", "surgical"), ("night", "an"), ("night", "stay")
        ]
        
        for shift, department in all_shifts:
            # 跳過週二、週三、週四的中午班（標記為"X"）
            if department == 'noon' and day_of_week in [1, 2, 3]:
                continue
            slots.append((day_index, shift, department))
    
    return slots

def can_assign_person_to_slot(person, day_index, shift, department, assigned_today):
    """檢查是否可以將人員分配到指定班次"""
    if person["work_times"] >= person["times"]:
        return False
    if person["name"] in assigned_today:
        return False
    if not can_work_shift(person, day_index, shift):
        return False
    return True

def calculate_slot_difficulty(day_index, shift, department):
    """計算班次的難度分數（分數越高越難填補）"""
    difficulty = 0
    
    # 夜班比日班難填補
    if shift == "night":
        difficulty += 10
    
    # 專科班次難度
    if department in ["internal", "surgical", "an"]:
        difficulty += 5
    
    # 月底更難填補
    difficulty += day_index * 0.1
    
    return difficulty

def assign_schedule_backtrack():
    """使用回溯法進行最優排班分配"""
    
    # 重置所有人員的工作次數
    for person in people:
        person["work_times"] = 0
    
    # 清空所有班次
    for day in schedule:
        for shift in ["day", "night"]:
            for dept in day[shift]:
                if day[shift][dept] != "X":
                    day[shift][dept] = ""
    
    # 獲取所有需要分配的班次，按難度排序
    slots = get_all_slots()
    slots.sort(key=lambda x: calculate_slot_difficulty(x[0], x[1], x[2]), reverse=True)
    
    def backtrack(slot_index):
        """回溯函數"""
        if slot_index == len(slots):
            return True  # 所有班次都分配完成
        
        day_index, shift, department = slots[slot_index]
        
        # 獲取當天已分配的人員
        assigned_today = set()
        for s in ["day", "night"]:
            for d in schedule[day_index][s]:
                if schedule[day_index][s][d] and schedule[day_index][s][d] != "X":
                    assigned_today.add(schedule[day_index][s][d])
        
        # 獲取可用人員列表，按優先級排序
        available_people = get_available_people_for_slot(day_index, shift, department, assigned_today)
        
        # 嘗試每個可用人員
        for person in available_people:
            # 分配這個人員
            schedule[day_index][shift][department] = person["name"]
            person["work_times"] += 1
            
            # 遞歸處理下一個班次
            if backtrack(slot_index + 1):
                return True
            
            # 回溯：撤銷分配
            schedule[day_index][shift][department] = ""
            person["work_times"] -= 1
        
        return False  # 無法找到合適的分配
    
    # 開始回溯
    success = backtrack(0)
    return success

def assign_schedule_hybrid():
    """使用混合策略：先用貪婪演算法，失敗後用回溯法"""
    
    print("第一階段：使用貪婪演算法...")
    
    # 重置所有人員的工作次數
    for person in people:
        person["work_times"] = 0
    
    # 清空所有班次
    for day in schedule:
        for shift in ["day", "night"]:
            for dept in day[shift]:
                if day[shift][dept] != "X":
                    day[shift][dept] = ""
    
    # 定義班次優先級（難填補的班次優先）
    shift_priority = [
        ("night", "internal"), ("night", "surgical"), ("night", "an"),
        ("day", "internal"), ("day", "surgical"), ("day", "an"),
        ("night", "stay"), ("day", "noon")
    ]
    
    for day_index, day in enumerate(schedule):
        assigned_today = set()
        
        # 按優先級處理每個班次
        for shift, department in shift_priority:
            # 跳過週二、週三、週四標記為"X"的中午班
            if department == 'noon' and day[shift][department] == 'X':
                continue
            
            # 如果班次已經被分配，跳過
            if day[shift][department] != "":
                continue
            
            # 獲取可用人員列表
            available_people = get_available_people_for_slot(day_index, shift, department, assigned_today)
            
            # 分配給最優先的人員
            if available_people:
                selected_person = available_people[0]
                day[shift][department] = selected_person["name"]
                selected_person["work_times"] += 1
                assigned_today.add(selected_person["name"])
    
    # 檢查是否有空班
    empty_count, total_shifts, empty_details = count_empty_shifts()
    
    if empty_count == 0:
        print("貪婪演算法成功！無空班。")
        return True
    else:
        print(f"貪婪演算法結果：{empty_count} 個空班")
        print("第二階段：使用回溯法尋找完美解...")
        
        # 使用回溯法
        success = assign_schedule_backtrack()
        if success:
            print("回溯法成功！找到完美解。")
            return True
        else:
            print("回溯法失敗：無法找到完美解。")
            return False

# 使用混合策略進行排班
def assign_schedule():
    """主排班函數"""
    return assign_schedule_hybrid()

def count_empty_shifts():
    """統計空班數量"""
    empty_count = 0
    total_shifts = 0
    empty_details = []
    
    for i, day in enumerate(schedule):
        date = day["date"]
        current_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        day_of_week = current_date.weekday()
        
        # 檢查所有班次
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
            # 週二、週三、週四的中午班標記為"X"，不算在統計內
            if department == 'noon' and day_of_week in [1, 2, 3]:
                continue
                
            total_shifts += 1
            if day[shift][department] == "":
                empty_count += 1
                empty_details.append(f"第{i+1}天 ({date}) - {shift_name}")
    
    return empty_count, total_shifts, empty_details

# 執行混合策略排班
print("正在執行混合策略排班（貪婪 + 回溯）...")
success = assign_schedule()

def display_results():
    """顯示排班結果和統計"""
    print("=" * 60)
    print("混合策略排班結果")
    print("=" * 60)
    
    # 統計空班
    empty_count, total_shifts, empty_details = count_empty_shifts()
    coverage_rate = (total_shifts - empty_count) / total_shifts * 100
    
    print(f"\n班次覆蓋率統計：")
    print(f"總班次數: {total_shifts}")
    print(f"已分配班次: {total_shifts - empty_count}")
    print(f"空班數: {empty_count}")
    print(f"覆蓋率: {coverage_rate:.1f}%")
    
    if empty_details:
        print(f"\n空班詳情：")
        for detail in empty_details:
            print(f"  - {detail}")
    else:
        print("\n🎉 完美排班！沒有空班！")
    

# 顯示優化結果
display_results()

# 印出工作分配摘要
print("工作分配摘要：")
for person in people:
    print(f"{person['name']}: {person['work_times']}/{person['times']} 班次已分配")

print("\n排班表：")
for i, day in enumerate(schedule):
    print(f"第{i+1}天 ({day['date']})：")
    print(f"  日班 - 內科: {day['day']['internal']}, 外科: {day['day']['surgical']}, 安康: {day['day']['an']}, 中午: {day['day']['noon']}")
    print(f"  夜班 - 內科: {day['night']['internal']}, 外科: {day['night']['surgical']}, 安康: {day['night']['an']}, 留守: {day['night']['stay']}")
    print()

# 顯示排班結果和統計
display_results()










































