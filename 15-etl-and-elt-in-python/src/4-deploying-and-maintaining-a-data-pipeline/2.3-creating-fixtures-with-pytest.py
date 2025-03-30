# Import pytest
import pytest

def extract(file_path):
    return pd.read_csv(file_path)

# Create a pytest fixture
@pytest.fixture()
def raw_tax_data():
	raw_data = extract("raw_tax_data.csv")
    
    # Return the raw DataFrame
	return raw_data