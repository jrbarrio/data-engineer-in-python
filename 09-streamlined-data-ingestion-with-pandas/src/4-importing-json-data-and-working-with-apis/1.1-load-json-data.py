# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json('./09-streamlined-data-ingestion-with-pandas/files/dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())