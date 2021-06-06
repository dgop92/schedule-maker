import json

def load_data_from_json_file(file_path):
    with open(file_path, 'r', encoding='utf8') as read_file:
        return json.load(read_file)

def write_json_from_dict(file_path, data): 
    with open(file_path, "w", encoding='utf8') as write_file:
        json.dump(data, write_file, indent=4, ensure_ascii=False)
