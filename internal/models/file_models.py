from abc import ABC, abstractmethod
from typing import List
import csv
import os

class File(ABC):

    @abstractmethod
    def ReadFile(self) -> List[List[str]]:
        pass

class FileCSV(File):
    def __init__(self, path: str, name: str):
        self.path = path
        self.name = name

    def ReadFile(self) -> List[List[str]]:
        full_path = os.path.join(self.path, self.name)

        try:
            with open(full_path, 'r', newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)

                next(csv_reader, None)
                
                return list(csv_reader)     
        except FileNotFoundError:
            print(f"Ошибка: Файл '{full_path}' не найден")
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []