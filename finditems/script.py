import os
import json

search_string = input("Enter the search string: ")
if not search_string.startswith("minecraft:"):
    search_string = "minecraft:" + search_string

current_dir = os.getcwd()
num_found_files = 0

def check_file_for_string(file_path):
    global num_found_files
    with open(file_path, "r") as f:
        data = json.load(f)
        str_data = json.dumps(data)
        if search_string in str_data:
            rel_path = os.path.relpath(file_path, current_dir)
            num_found_files += 1
            print("...\\" + rel_path)

def search_dir_for_string(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                check_file_for_string(file_path)

search_dir_for_string(current_dir)
print("Found", num_found_files, "files containing '", search_string, "'.")
