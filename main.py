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
        "day": {"internal": "", "surgical": "", "an": "", "noon": ""},  # 日班：內科、外科、麻醉科、中午班
        "night": {"internal": "", "surgical": "", "an": "", "stay": ""}  # 夜班：內科、外科、麻醉科、留守班
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
                "an": "",         # 麻醉科日班
                "noon": noon_value # 中午班
            },
            "night": {
                "internal": "",   # 內科夜班
                "surgical": "",   # 外科夜班
                "an": "",        # 麻醉科夜班
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
"work":"an",          # 工作類型：麻醉科
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

def assign_schedule():
    """根據每個人的可用性和工作類型分配排班
    
    這個函數會遍歷每一天，並根據以下邏輯分配人員：
    1. 首先分配專科人員（內科、外科、麻醉科）
    2. 然後分配靈活人員（工作類型為"ok"）
    3. 最後分配中午班和留守班
    """
    
    for day_index, day in enumerate(schedule):
        # 分配內科醫師
        for person in people:
            if person["work"] == "internal" and person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                # 根據可用性分配班次
                if availability == "no_night" and day["day"]["internal"] == "":
                    day["day"]["internal"] = person["name"]
                    person["work_times"] += 1
                elif availability == "no_day" and day["night"]["internal"] == "":
                    day["night"]["internal"] = person["name"]
                    person["work_times"] += 1
                elif availability == "ok":
                    if day["day"]["internal"] == "":
                        day["day"]["internal"] = person["name"]
                        person["work_times"] += 1
                    elif day["night"]["internal"] == "":
                        day["night"]["internal"] = person["name"]
                        person["work_times"] += 1
                elif availability == "work-no_night" and day["day"]["internal"] == "":
                    day["day"]["internal"] = person["name"]
                    person["work_times"] += 1
        
        # 分配外科醫師
        for person in people:
            if person["work"] == "surgical" and person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                if availability == "no_night" and day["day"]["surgical"] == "":
                    day["day"]["surgical"] = person["name"]
                    person["work_times"] += 1
                elif availability == "no_day" and day["night"]["surgical"] == "":
                    day["night"]["surgical"] = person["name"]
                    person["work_times"] += 1
                elif availability == "ok":
                    if day["day"]["surgical"] == "":
                        day["day"]["surgical"] = person["name"]
                        person["work_times"] += 1
                    elif day["night"]["surgical"] == "":
                        day["night"]["surgical"] = person["name"]
                        person["work_times"] += 1
        
        # 分配麻醉科醫師
        for person in people:
            if person["work"] == "an" and person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                if availability == "no_night" and day["day"]["an"] == "":
                    day["day"]["an"] = person["name"]
                    person["work_times"] += 1
                elif availability == "no_day" and day["night"]["an"] == "":
                    day["night"]["an"] = person["name"]
                    person["work_times"] += 1
                elif availability == "ok":
                    if day["day"]["an"] == "":
                        day["day"]["an"] = person["name"]
                        person["work_times"] += 1
                    elif day["night"]["an"] == "":
                        day["night"]["an"] = person["name"]
                        person["work_times"] += 1
        
        # 分配靈活人員（工作類型為"ok"的人員）填補剩餘職位
        for person in people:
            if person["work"] == "ok" and person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                if availability == "no_night":
                    # 優先填補日班
                    if day["day"]["internal"] == "":
                        day["day"]["internal"] = person["name"]
                        person["work_times"] += 1
                    elif day["day"]["surgical"] == "":
                        day["day"]["surgical"] = person["name"]
                        person["work_times"] += 1
                    elif day["day"]["an"] == "":
                        day["day"]["an"] = person["name"]
                        person["work_times"] += 1
                elif availability == "no_day":
                    # 填補夜班
                    if day["night"]["internal"] == "":
                        day["night"]["internal"] = person["name"]
                        person["work_times"] += 1
                    elif day["night"]["surgical"] == "":
                        day["night"]["surgical"] = person["name"]
                        person["work_times"] += 1
                    elif day["night"]["an"] == "":
                        day["night"]["an"] = person["name"]
                        person["work_times"] += 1
                elif availability == "ok":
                    # 填補任何可用的職位
                    slots_to_fill = [
                        ("day", "internal"), ("day", "surgical"), ("day", "an"),
                        ("night", "internal"), ("night", "surgical"), ("night", "an"), ("night", "stay")
                    ]
                    for shift, department in slots_to_fill:
                        if day[shift][department] == "":
                            day[shift][department] = person["name"]
                            person["work_times"] += 1
                            break
        
        # 分配中午班（僅限能上日班的人員）
        for person in people:
            if person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                # 只有能上日班且中午班為空且不是標記為"X"的日子才分配中午班
                if (availability in ["ok", "no_night", "work-no_night"] and 
                    day["day"]["noon"] == "" and 
                    day_index < len(schedule)):
                    
                    # 檢查是否為需要中午班覆蓋的工作日（週二、週三、週四標記為"X"）
                    current_date = datetime.datetime.strptime(day["date"], "%Y-%m-%d")
                    day_of_week = current_date.weekday()
                    
                    # 如果不是週二、週三、週四，可以分配人員
                    if day_of_week not in [1, 2, 3]:
                        day["day"]["noon"] = person["name"]
                        person["work_times"] += 1
                        # 中午班可能是較輕的工作，所以不計入work_times
        
        # 分配留守班（夜間值班）
        for person in people:
            if person["work_times"] < person["times"]:
                availability = person["days"][day_index]
                
                if (availability in ["ok", "no_day"] and 
                    day["night"]["stay"] == ""):
                    day["night"]["stay"] = person["name"]
                    # 留守班可能是較輕的工作，所以不計入work_times

# 執行排班演算法
assign_schedule()

# 印出工作分配摘要
print("工作分配摘要：")
for person in people:
    print(f"{person['name']}: {person['work_times']}/{person['times']} 班次已分配")

print("\n排班表：")
for i, day in enumerate(schedule):
    print(f"第{i+1}天 ({day['date']})：")
    print(f"  日班 - 內科: {day['day']['internal']}, 外科: {day['day']['surgical']}, 麻醉: {day['day']['an']}, 中午: {day['day']['noon']}")
    print(f"  夜班 - 內科: {day['night']['internal']}, 外科: {day['night']['surgical']}, 麻醉: {day['night']['an']}, 留守: {day['night']['stay']}")
    print()










































