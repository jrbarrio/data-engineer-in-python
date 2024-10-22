# Import pandas
import matplotlib.pyplot as plt
import pandas as pd


# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('./04-introduction-to-importig-data-in-python/files/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()