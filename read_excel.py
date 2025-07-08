import pandas as pd

# Read the Excel file
df = pd.read_excel('excel.xlsx')

value = df.iloc[19]

value_list = value.tolist()
print(value_list)