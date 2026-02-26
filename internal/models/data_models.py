class Data():
    def __init__(self, country: str = "", year: int = 0, gdp: int = 0,
                gdp_growth: float = 0.0, inflation: float = 0.0, unemployment: float = 0.0,
                population: int = 0, continent: str = ""):
        self._country = country
        self._year = year
        self._gdp = gdp
        self._gdp_growth = gdp_growth
        self._inflation = inflation 
        self._unemployment = unemployment
        self._population = population
        self._continent = continent

    def GetCountry(self):
        return self._country
    
    def GetGdp(self):
        return self._gdp
    
    def __str__(self) -> str:
        return (f"Страна: {self._country}, Год: {self._year}, "
                f"ВВП: {self._gdp} млрд, Рост: {self._gdp_growth}%, "
                f"Инфляция: {self._inflation}%, Безработица: {self._unemployment}%, "
                f"Население: {self._population} млн, Континент: {self._continent}")