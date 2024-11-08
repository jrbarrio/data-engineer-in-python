import pandas as pd
import matplotlib.pyplot as plt

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                                skiprows=2,
                                sheet_name=['2016', '2017'])

# View the data type of all_survey_data
print(all_survey_data.keys())

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                                sheet_name=[0, '2017'])

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                                sheet_name=None)

# View the sheet names in all_survey_data
print(all_survey_data.keys())