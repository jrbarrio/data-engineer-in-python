# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = './04-introduction-to-importig-data-in-python/files/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)