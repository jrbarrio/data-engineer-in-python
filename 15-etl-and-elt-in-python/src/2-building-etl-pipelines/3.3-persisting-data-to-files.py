def load(clean_data, file_path):
    # Write the data to a file
    clean_data.to_csv(file_path, header=False, index=False)

    # Check to make sure the file exists
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load(clean_sales_data, "transformed_sales_data.csv")