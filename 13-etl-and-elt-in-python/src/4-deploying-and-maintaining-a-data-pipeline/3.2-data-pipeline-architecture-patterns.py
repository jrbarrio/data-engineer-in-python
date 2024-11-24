# Import the extract, transform, and load functions from pipeline_utils
from pipeline_utils import extract, transform, load

# Run the pipeline end to end by extracting, transforming and loading the data
raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "clean_tax_data.parquet")