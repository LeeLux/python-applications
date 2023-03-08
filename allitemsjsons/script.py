import json
import os

# Create the out folder if it doesn't exist
if not os.path.exists("out"):
    os.makedirs("out")

# Read in the all.json file
with open("all.json", "r") as all_file:
    values = json.load(all_file)["values"]

# Create an empty JSON object to write to each file
empty_json = ""

# Iterate over the values list and create a new empty file for each value
for value in values:
    filename = f"{value.split(':')[1]}.json"
    filepath = os.path.join("out", filename)
    with open(filepath, "w") as value_file:
        value_file.write(empty_json)

# Print the number of files created
print(f"{len(values)} JSON files created successfully!")