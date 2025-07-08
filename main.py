import datetime

def create_month(year, month_num):
    month = []
    
    # Create a template for a day
    day_template = {
        "date": "",
        "day": {"internal": "", "surgical": "", "an": "", "noon": ""},
        "night": {"internal": "", "surgical": "", "an": "", "stay": ""}
    }
    
    # Get the first day of the specified month
    first_day = datetime.datetime(year, month_num, 1)
    
    # Get the number of days in the month
    if month_num == 12:
        next_month = datetime.datetime(year + 1, 1, 1)
    else:
        next_month = datetime.datetime(year, month_num + 1, 1)
    
    num_days = (next_month - first_day).days
    
    # Create days for the entire month
    for i in range(num_days):
        # Calculate the date for this day
        current_date = first_day + datetime.timedelta(days=i)
        
        # Create a new day by copying the template
        new_day = {
            "date": current_date.strftime("%Y-%m-%d"),
            "day": {
                "internal": "",
                "surgical": "",
                "an": "",
                "noon": ""
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

# Example usage:
current_year = datetime.datetime.now().year
july = create_month(current_year, 7)  # Create May
print(july)  # Print the created month


jian = {    
"name": "Jian",
"work":"internal",
"days": ["no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","off","off","off","off","off","off","off","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night","no_night",],
}
feng = {
"name": "Feng",
"work":"ok",
"days":["ok","ok","off","ok","ok","ok","ok","off","ok","ok","off","off","off","ok","off","ok","ok","off","ok","off","ok","ok","ok","off","ok","ok","off","ok","ok","ok","ok",]
 }
ming = {
"name": "Ming",
"work":"internal",
"days": ["ok","ok","ok","ok","off","ok","ok","off","ok","ok","ok","ok","off","ok","no_day","ok","no_day""ok","ok","ok","ok","no_day","ok","ok","ok","ok","ok","ok","no_day","ok","no_day"]
}
lan = {
"name": "Lan",
"work":"internal",
"days": ['no_night', '上班', 'no_night', '上班', 'no_night', 'no_night', 'no_night', 'no_night', '上班', 'no_night', 'no_night', '上班', '上班', 'no_night', 'no_night', 'no_night', 'no_night', '上班', 'no_night', 'no_night', 'no_night', 'no_night', '上班', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', '上班',"no_night"]
}
mou = {
"name": "Mou",
"work":"an",
"days": ['no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'OFF', 'no_night', 'no_night', 'no_night']
}
teng ={
"name": "Teng",
"work":"ok",
"days": ['no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'OFF', 'OFF', 'no_night', 'no_night', 'no_night', 'no_night',]
}
zhi = {
"name": "Zhi",
"work":"ok",
"days":['OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok',] 
}        
hua ={
"name": "Hua",
"work":"ok",
"days":['ok', 'ok', 'OFF', 'no_day', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'no_day', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', ]
}
da = {
"name": "Da",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF',]
}
jin = {
"name": "Jin",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'no_night', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'no_day', 'ok', 'ok', 'ok', 'ok', 'ok', ]
}
yong ={
"name": "Yong",
"work":"ok",    
"days":['OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', ]
}
yi = {
"name": "Yi",
"work":"ok",
"days":['OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok',]
}
fang = {
"name": "Fang",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'no_night', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF',]
}
han = {
"name": "Han",
"work":"ok",
"days":['OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', ]
}
chun = {
"name": "Chun",
"work":"surgical",
"days":['no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', 'no_night', ]
}
jian2 = {
"name": "Jian2",
"work":"ok",  
"days":['ok', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'OFF', 'ok', 'ok', 'ok', 'OFF', 'ok', 'ok', 'ok', 'ok', 'ok',]
}
qiang = {
"name": "qiang",
"work":"ok",
"days":['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok',]
}














































