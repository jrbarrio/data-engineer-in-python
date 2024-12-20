# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx")

# View the head of the dataframe
print(survey_responses.head())