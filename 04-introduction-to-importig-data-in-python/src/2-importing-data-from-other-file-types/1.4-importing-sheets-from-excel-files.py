# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = './04-introduction-to-importig-data-in-python/files/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())