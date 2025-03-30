import pandas as pd
import matplotlib.pyplot as plt

# Load the data
survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                          usecols=["ID.x", "HasDebt", "HasFinancialDependents", "HasHomeMortgage", "HasStudentDebt"])

# Count NA values in each column
print(survey_data.isna().sum())

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                          usecols=["ID.x", "HasDebt", "HasFinancialDependents", "HasHomeMortgage", "HasStudentDebt"],
                          dtype={"HasDebt": bool, "AttendedBootCampYesNo": bool})

# View financial burdens by Boolean group
print(survey_data.head)

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                          usecols=["ID.x", "HasDebt", "HasFinancialDependents", "HasHomeMortgage", "HasStudentDebt"],
                          dtype={"HasDebt": bool, "AttendedBootCampYesNo": bool},
                          true_values=["Yes"],
                          false_values=["No"])

# View the data
print(survey_subset.head())