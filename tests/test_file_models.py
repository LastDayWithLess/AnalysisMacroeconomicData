import pytest
import csv
from internal.models.file_models import FileCSV

class TestFileCSV:
    
    def test_init(self):
        """Тест инициализации"""
        file = FileCSV("/test/path", "test.csv")
        assert file.path == "/test/path"
        assert file.name == "test.csv"
    
    def test_read_file_success(self, tmp_path):
        """Тест успешного чтения файла"""

        test_file = tmp_path / "test.csv"
        with open(test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['country', 'year', 'gdp', 'gdp_growth', 'inflation', 'unemployment', 'population', 'continent'])
            writer.writerow(['Russia', '2023', '2000.0', '2.5', '5.0', '4.5', '146', 'Europe'])
            writer.writerow(['USA', '2023', '26350.0', '2.1', '3.4', '3.7', '334', 'North America'])
        
        file = FileCSV(str(tmp_path), "test.csv")
        result = file.ReadFile()
        
        assert len(result) == 2
        assert result[0][0] == "Russia"
        assert result[1][0] == "USA"
    
    def test_read_file_not_found(self):
        """Тест чтения несуществующего файла"""
        file = FileCSV("/invalid/path", "nonexistent.csv")
        result = file.ReadFile()
        assert result == []
    
    def test_read_file_empty(self, tmp_path):
        """Тест чтения пустого файла"""
        empty_file = tmp_path / "empty.csv"
        empty_file.write_text("country,year,gdp,gdp_growth,inflation,unemployment,population,continent\n")
        
        file = FileCSV(str(tmp_path), "empty.csv")
        result = file.ReadFile()
        assert result == []
