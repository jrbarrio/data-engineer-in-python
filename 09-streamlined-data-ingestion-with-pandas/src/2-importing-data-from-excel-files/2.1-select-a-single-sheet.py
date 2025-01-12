# Load pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("./09-streamlined-data-ingestion-with-pandas/files/fcc-new-coder-survey.xlsx",
                               skiprows=2,
                               sheet_name=1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name="2017")

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()