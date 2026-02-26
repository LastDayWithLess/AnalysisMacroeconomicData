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
        %(prog)s --files /home/kirill/Загрузки --report economic2.csv
        %(prog)s --files ./data --report stats.csv
        '''
    )
    
    parser.add_argument(
        '--files',
        type=str,
        required=True,
        help='Путь к директории с файлами (обязательно)'
    )
    
    parser.add_argument(
        '--report',
        nargs='+', 
        type=str,
        required=True,
        help='Имя CSV файла(ов) (обязательно)'
    )

    valid_args = ['--files', '--report']
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith('--'):
            if arg not in valid_args:
                print(f"Ошибка: Неизвестный аргумент '{arg}'")
                print(f"Допустимые аргументы: --files, --report")
                print(f"\nПример правильного вызова:")
                print(f"  python3 -m app.main --files /home/kirill/Загрузки --report economic2.csv")
                sys.exit(1)
            if i + 1 < len(sys.argv) and not sys.argv[i + 1].startswith('--'):
                i += 1
        i += 1
    
    args = parser.parse_args()
    return args

def validate_files(path, filenames):
    missing = []
    for filename in filenames:
        full_path = os.path.join(path, filename)
        if not os.path.isfile(full_path):
            missing.append(filename)
    
    if missing:
        print("Ошибка: Следующие файлы не найдены:")
        for f in missing:
            print(f"  - {f}")
        return False
    return True

def validate_csv_extension(filenames):
    invalid = []
    for filename in filenames:
        if not filename.lower().endswith('.csv'):
            invalid.append(filename)
    
    if invalid:
        print("Ошибка: Файлы должны иметь расширение .csv:")
        for f in invalid:
            print(f"  - {f}")
        return False
    return True

def Run():
    try:
        args = parse_arguments()
    except SystemExit:
        return
    
    if not os.path.exists(args.files):
        print(f"Ошибка: Путь '{args.files}' не существует")
        return
    
    if not os.path.isdir(args.files):
        print(f"Ошибка: '{args.files}' не является директорией")
        return
    
    if not validate_csv_extension(args.report):
        return
    
    if not validate_files(args.files, args.report):
        return

    
    all_results = []
    
    for filename in args.report:
        f = model.FileCSV(args.files, filename)
        data_list = f.ReadFile()
        
        if not data_list:
            print(f"Файл {filename} пуст или не удалось прочитать данные")
            continue
        
        parse = data_parser.DataParser.Parse(data_list)
        
        if not parse:
            print(f"Нет данных для парсинга в файле {filename}")
            continue
        
        result = data_analyzer.DataAnalyzer.CalculateAvgGdp(parse)
        
        if not result:
            print(f"Нет данных для анализа в файле {filename}")
            continue
        
        all_results.append({
            'file': filename,
            'data': result
        })
    
    if not all_results:
        print("\nНет данных для отображения")
        return
    
    
    for file_result in all_results:
        table_data = []
        
        if isinstance(file_result['data'], dict):
            for country, avg_gdp in file_result['data'].items():
                table_data.append([country, avg_gdp])
        else:
            for item in file_result['data']:
                if isinstance(item, (list, tuple)) and len(item) >= 2:
                    table_data.append([item[0], item[1]])
        
        table_data.sort(key=lambda x: x[1], reverse=True)
        
        print(tabulate(
            table_data,
            headers=['Страна', 'Средний ВВП'],
            tablefmt="grid",
            floatfmt=".2f",
            numalign="right"
        ))
