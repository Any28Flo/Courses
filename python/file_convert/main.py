# This is a sample Python script.
import json
from pathlib import Path


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_file(path):
    """Function to read files"""
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        return content


def read_json_data(data):
    """Parse json to data"""
    return json.loads('[{}]'.format(data))


def parse_json_data(content):
    """Parse data to json"""
    return json.dumps(content)


def add_key_value(object, key, value):
    new_obj = object
    new_obj[key] = value
    return new_obj


# Load files to parse
files = ['datas.json', 'medicos_data.json']

path = Path('user_data.json')

data = []

for file in files:
    content_file = read_file(file)
    str_data = read_json_data(content_file)
    if file == 'datas.json':

        for item in str_data:
            print(len(item["Medicos"]))
            i = 0
            while i < len(item["Medicos"]):
                obj = item["Medicos"][i]
                obj_updated = add_key_value(obj, "tipo", "clinica")

                data.append(obj_updated)

                i += 1
    elif file == "medicos_data.json":
        print(file)

        for item2 in str_data:
            print(len(item2["Medicos"]))
            i = 0
            while i < len(item2["Medicos"]):
                obj = item2["Medicos"][i]
                obj_updated = add_key_value(obj, "tipo", "medico")

                data.append(obj_updated)
                i += 1

    content = parse_json_data(data)
    path.write_text(content)
    print(f"end {file} parse json")

# while i < len(item["Medicos"]):
#    i += 1
#  for key, value in item["Medicos"][0]:
#     print(f"{key}:{value}")

# for each file parse json to data
# content = read_json_data(file)
