@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("raw_tax_data.csv")
    clean_data = transform(raw_data)
    return clean_data

# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert clean_tax_data["tax_rate"].max() <= 1 and clean_tax_data["tax_rate"].min() >= 0