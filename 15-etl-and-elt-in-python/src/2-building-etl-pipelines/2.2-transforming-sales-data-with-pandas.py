raw_sales_data = extract("sales_data.csv")

def transform(raw_data):
    # Convert the "Order Date" column to type datetime
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    
    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    return clean_data

clean_sales_data = transform(raw_sales_data)

# Check the data types of each column
print(clean_sales_data.dtypes)