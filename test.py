import datetime
import json

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

scheduleData = {
    "year": 2025,      
    "month": 7,
    "people": people
}

with open("scheduleData.json", "w", encoding="utf-8") as f:
    json.dump(scheduleData, f, ensure_ascii=False, indent=2)