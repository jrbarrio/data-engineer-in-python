import pytest

def transform(raw_data):
    raw_data["average_taxable_income"] = raw_data["total_taxable_income"] / raw_data["number_of_firms"]
    clean_data = raw_data.loc[raw_data["average_taxable_income"] > 100, :]
    clean_data.set_index("industry_name", inplace=True)
    return clean_data

def test_transformed_data():
    raw_tax_data = extract("raw_tax_data.csv")
    clean_tax_data = transform(raw_tax_data)
    
    # Assert that the transform function returns a pd.DataFrame
    assert isinstance(clean_tax_data, pd.DataFrame)
    
    # Assert that the clean_tax_data DataFrame has more columns than the raw_tax_data DataFrame
    assert len(clean_tax_data.columns) > len(raw_tax_data.columns)