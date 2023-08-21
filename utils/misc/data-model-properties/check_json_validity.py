import os
import json

def is_valid_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
            return True
    except (ValueError, UnicodeDecodeError):
        return False

def validate_json_files_in_folder(folder_path, output_file):
    with open(output_file, 'w') as out_file:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                if file_name.endswith('.jsonld'):
                    file_path = os.path.join(root, file_name)
                    if is_valid_json(file_path):
                        out_file.write(f"{file_path}: Valid JSON\n")
                    else:
                        out_file.write(f"{file_path}: Invalid JSON\n")

if __name__ == "__main__":
    folder_path = "/home/monika/Documents/AGRI-VOC/agri-voc/data-models"

    output_file = "json_validity.txt"
    validate_json_files_in_folder(folder_path, output_file)
    print(f"Validation results written to {output_file}")

