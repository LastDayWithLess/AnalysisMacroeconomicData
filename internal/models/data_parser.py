from typing import List
import internal.models.data_models as data_models

class DataParser:
    @staticmethod 
    def Parse(data: List[List[str]]) -> List[data_models.Data]:
        data_list: List[data_models.Data] = []
        
        for row in data:
            if len(row) >= 8:
                try:
                    data_obj = data_models.Data(
                        country=row[0],
                        year=int(row[1]),
                        gdp=float(row[2]),
                        gdp_growth=float(row[3]),
                        inflation=float(row[4]),
                        unemployment=float(row[5]),
                        population=int(row[6]),
                        continent=row[7]
                    )
                    data_list.append(data_obj)
                except (ValueError, IndexError) as e:
                    print(f"Ошибка парсинга строки {row}: {e}")
        
        return data_list