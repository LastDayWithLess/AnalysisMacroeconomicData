from typing import List, Dict, Any
import internal.models.data_models as data_models

class CompositeData():
    def __init__(self, gdp: float = 0):
        self.gdp = gdp
        self.count = 0

    def GetGdp(self):
        return self.gdp
    
    def add_value(self, gdp_value: float):
        self.gdp += gdp_value
        self.count += 1

class DataAnalyzer:
    
    @staticmethod
    def CalculateAvgGdp(data_list: List[data_models.Data]) -> List[List[Any]]:
        if not data_list:
            return []
        
        result: Dict[str, CompositeData] = {}
        
        for data in data_list:
            continent = data.GetCountry()
            
            if continent not in result:
                result[continent] = CompositeData()
            
            result[continent].add_value(data.GetGdp())

        table_data = []

        for key, value in result.items():
            avg = value.gdp / value.count
            table_data.append([key, avg])
        
        return table_data

