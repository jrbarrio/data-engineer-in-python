# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
file = './05-intermediate-importing-data-in-python/files/winequality-red.csv'

# Save file locally
urlretrieve(url, file)

# Read file into a DataFrame and print its head
df = pd.read_csv(file, sep=';')
print(df.head())