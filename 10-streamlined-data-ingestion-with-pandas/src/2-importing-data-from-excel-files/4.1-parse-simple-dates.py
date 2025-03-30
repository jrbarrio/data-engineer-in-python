import pandas as pd

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                           parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())