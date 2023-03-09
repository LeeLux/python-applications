import os
import json

search_string = input("Enter the search string: ")
if not search_string.startswith("minecraft:"):
    search_string = "minecraft:" + search_string

current_dir = os.getcwd()
num_found_files = 0
supported_filetypes = [".json", ".mcfunction"]

def check_file_for_string(file_path):
    global num_found_files
    with open(file_path, "r") as f:
        data = f.read()
        if file_path.endswith(".json"):
            try:
                data = json.loads(data)
                str_data = json.dumps(data)
            except:
                return
        elif file_path.endswith(".mcfunction"):
            str_data = data
        else:
            return
        if search_string.lower() in str_data.lower():
            rel_path = os.path.relpath(file_path, current_dir)
            print("...\\" + rel_path)
            num_found_files += 1

def search_dir_for_string(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if any(file.endswith(ext) for ext in supported_filetypes):
                file_path = os.path.join(root, file)
                check_file_for_string(file_path)

search_dir_for_string(current_dir)
print("Found", num_found_files, "files containing '", search_string.lower(), "'.")
