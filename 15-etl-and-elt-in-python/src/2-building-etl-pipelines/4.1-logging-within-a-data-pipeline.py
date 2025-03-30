def transform(raw_data):
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    
    # Create an info log regarding transformation
    logging.info("Transformed 'Order Date' column to type 'datetime'.")
    
    # Create debug-level logs for the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of the DataFrame after filtering: {clean_data.shape}")
    
    return clean_data
  
clean_sales_data = transform(raw_sales_data)