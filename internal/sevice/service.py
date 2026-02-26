import internal.models.file_models as model
import internal.models.data_parser as data_parser
import internal.models.data_analyzer as data_analyzer
from tabulate import tabulate
import argparse
import sys
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Анализ CSV файла с экономическими данными',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
        Примеры использования:
        %(prog)s --files ./data --report stats.csv
                '''
    )
    
    parser.add_argument(
        '--files',
        type=str,
        required=True,
        help='Путь к директории с файлом (обязательно)'
    )
    
    parser.add_argument(
        '--report',
        nargs='+', 
        type=str,
        required=True,
        help='Имя CSV файла (обязательно)'
    )
    
    return parser.parse_args()

def Run():
    args = parse_arguments()
    
    for filename in args.report:
        f = model.FileCSV(args.files, filename)
        data_list = f.ReadFile()
    
    if not data_list:
        print("Файл пуст или не удалось прочитать данные")
        return
    
    parse = data_parser.DataParser.Parse(data_list)
    
    result = data_analyzer.DataAnalyzer.CalculateAvgGdp(parse)
    
    if not result:
        print("Нет данных для анализа")
        return
    
    table_data = []
    for country, avg_gdp in result:
        table_data.append([country, avg_gdp])
    
    table_data.sort(key=lambda x: x[1], reverse=True)
    
    print(tabulate(
        table_data,
        headers=['Страна', 'Средний ВВП'],
        tablefmt="grid",
        floatfmt=".2f",
        numalign="right"
    ))