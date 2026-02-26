import pytest
import sys
import os

from internal.models.data_analyzer import DataAnalyzer
from internal.models.data_models import Data

class TestDataAnalyzer:
    
    def test_calculate_avg_gdp(self):
        """Тест расчета среднего ВВП"""
        data_list = [
            Data("Russia", 2023, 2000.0, 2.5, 5.0, 4.5, 146, "Europe"),
            Data("USA", 2023, 26350.0, 2.1, 3.4, 3.7, 334, "North America"),
            Data("China", 2023, 17963.0, 5.2, 0.7, 5.2, 1412, "Asia"),
            Data("Germany", 2023, 4300.0, 0.3, 6.2, 3.1, 83, "Europe")
        ]
        
        result = DataAnalyzer.CalculateAvgGdp(data_list)
        
        assert isinstance(result, list)
        
        result_dict = dict(result)
        
        assert len(result_dict) == 4
        assert "Russia" in result_dict
        assert result_dict["Russia"] == 2000.0
        assert result_dict["USA"] == 26350.0
    
    def test_calculate_avg_gdp_empty(self):
        """Тест с пустым списком"""
        result = DataAnalyzer.CalculateAvgGdp([])
        assert result == [] 
    
    def test_calculate_avg_gdp_with_duplicates(self):
        """Тест с дублирующимися странами"""
        data_list = [
            Data("Russia", 2023, 2000.0, 2.5, 5.0, 4.5, 146, "Europe"),
            Data("Russia", 2022, 1800.0, 2.3, 4.5, 4.2, 146, "Europe"),
            Data("USA", 2023, 26350.0, 2.1, 3.4, 3.7, 334, "North America")
        ]
        
        result = DataAnalyzer.CalculateAvgGdp(data_list)
        result_dict = dict(result)
        
        assert result_dict["Russia"] == 1900.0
        assert result_dict["USA"] == 26350.0
    
    def test_calculate_avg_gdp_rounding(self):
        """Тест округления результатов"""
        data_list = [
            Data("Test", 2023, 1000.0, 2.5, 5.0, 4.5, 146, "Test"),
            Data("Test", 2022, 1000.0 / 3, 2.3, 4.5, 4.2, 146, "Test")
        ]
        
        result = DataAnalyzer.CalculateAvgGdp(data_list)
        result_dict = dict(result)
        
        assert round(result_dict["Test"], 2) == 666.67