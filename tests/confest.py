import pytest
import os
import tempfile
import csv
from internal.models.data_models import Data

@pytest.fixture
def sample_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['country', 'year', 'gdp', 'gdp_growth', 'inflation', 'unemployment', 'population', 'continent'])
        writer.writerow(['Russia', 2023, 2000.0, 2.5, 5.0, 4.5, 146, 'Europe'])
        writer.writerow(['USA', 2023, 26350.0, 2.1, 3.4, 3.7, 334, 'North America'])
        writer.writerow(['China', 2023, 17963.0, 5.2, 0.7, 5.2, 1412, 'Asia'])
        writer.writerow(['Germany', 2023, 4300.0, 0.3, 6.2, 3.1, 83, 'Europe'])
    
    yield f.name
    
    os.unlink(f.name)

@pytest.fixture
def sample_data_list():
    return [
        Data("Russia", 2023, 2000.0, 2.5, 5.0, 4.5, 146, "Europe"),
        Data("USA", 2023, 26350.0, 2.1, 3.4, 3.7, 334, "North America"),
        Data("China", 2023, 17963.0, 5.2, 0.7, 5.2, 1412, "Asia"),
        Data("Germany", 2023, 4300.0, 0.3, 6.2, 3.1, 83, "Europe")
    ]