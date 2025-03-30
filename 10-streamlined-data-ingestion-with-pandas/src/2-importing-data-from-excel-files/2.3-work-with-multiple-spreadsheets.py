import pandas as pd
import matplotlib.pyplot as plt

# Load all sheets in the Excel file
responses = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                          skiprows=2,
                          sheet_name=None)

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()