import os
import json
# Initialize variables to keep track of number of files modified and their paths
num_files_modified = 0
modified_file_paths = []

# Define function to modify json files
def modify_json_file(file_path):
    global num_files_modified
    global modified_file_paths

    # Load json data from file
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON data from file {file_path}: {e}")
        return

    # Check if json data has 'result' and 'type, field
    if 'result' in data and 'type' in data:

        # Check if 'result' field is a string or an object
        if isinstance(data['result'], dict):
            result_item = data['result']['item']
        else:
            result_item = data['result']

        # Check if file contains 'type' key
        keys = list(data.keys())
        if 'type' in keys:
            type_field_index = keys.index('type')
            if 'group' not in keys:
                # Add 'group' key after 'type' key
                data.update({'group': str(result_item).replace('minecraft:', '')})
                keys.insert(type_field_index+1, 'group')
                data = {k:data[k] for k in keys}
                # Update variables to keep track of modified files
                num_files_modified += 1
                modified_file_paths.append(os.path.relpath(file_path))

        # Save modified json data to file
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

# Define function to recursively search for json files in a directory and its subdirectories
def search_for_json_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            search_for_json_files(file_path)
        elif filename.endswith('.json'):
            modify_json_file(file_path)


# Call search_for_json_files function to start search from current directory
search_for_json_files(os.getcwd())

# Print number of files modified and their paths
for file_path in modified_file_paths:
    print('...\\', file_path)
print(num_files_modified, ' files modified.')