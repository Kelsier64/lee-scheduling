import pandas as pd

# Read the Excel file
df = pd.read_excel('excel.xlsx')

value = df.iloc[30]

value_list = value.tolist()



for i in range(len(value_list)):
    if pd.isna(value_list[i]):
        value_list[i] = "no_night"
print(value_list)
print(len(value_list))