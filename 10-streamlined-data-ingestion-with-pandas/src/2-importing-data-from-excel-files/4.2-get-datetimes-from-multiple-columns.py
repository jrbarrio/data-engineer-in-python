import pandas as pd

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", 
                                "Part2StartTime"]}

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                          parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())