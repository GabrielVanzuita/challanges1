##Utilizado para converter o arquivo CSV em JSON

import json
import csv


def json_converter(path_csv, save_path):
    with open(path_csv, 'r', encoding='utf-8') as file:
        data_csv = []
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data_csv.append(row)
    with open(save_path, "w", encoding='utf-8') as arquivo:
        json.dump(data_csv, arquivo, indent=4, ensure_ascii=False)

    print(f"Arquivo JSON salvo com sucesso em: {save_path}")

path_csv = r""
save_path = r""
json_converter(path_csv, save_path)
