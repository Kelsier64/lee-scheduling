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
"days": [],
}

