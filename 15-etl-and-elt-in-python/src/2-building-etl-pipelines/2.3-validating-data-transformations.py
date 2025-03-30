def extract(file_path):
    raw_data = pd.read_parquet(file_path)
    return raw_data

raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Filter rows and columns
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] == 1, ["Order ID", "Price Each", "Quantity Ordered"]]
    return clean_data

# Transform the raw_sales_data
clean_sales_data = transform(raw_sales_data)