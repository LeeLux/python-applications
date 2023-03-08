#written moastly by ChatGPT in 2023
import os

# Ask user for file/folder path, file format, and lines to add/remove
file_path = input("Enter file or folder path (press enter for current directory): ")
if not file_path:
    file_path = os.getcwd()
print(f"Selected path: {file_path}")
file_format = input("Enter file format (e.g. txt): ")
target_files = 0
for root, dirs, files in os.walk(file_path):
    for file in files:
        if file.endswith("." + file_format):
            target_files += 1
print(f"{target_files} {file_format} files found")
lines = input("Enter lines to add/remove (comma-separated): ").split(",")
print("Preview:\n")
for line in lines:
    print(line.strip())
print("\n")
remove_lines = input("Remove lines from file? (y/n): ").lower() == "y"
if remove_lines:
    print("Removing the string(s) from the file...")
else:
    print("Adding the string(s) to the file...")

# Initialize stats counters
total_files = 0
target_files = 0
files_modified = 0

# If file_path is a file, process that file only
if os.path.isfile(file_path):
    print("Path is a file...")
    total_files += 1
    if file_path.endswith("." + file_format):
        target_files += 1
        with open(file_path, "r+") as f:
            content = f.read()
            if remove_lines:
                for line in lines:
                    if line + "\n" in content:
                        content = content.replace(line + "\n", "", 1)
                files_modified += 1
                f.seek(0)
                f.write(content)
                f.truncate()
            else:
                first_line = f.readline().strip()
                if first_line not in lines:
                    f.seek(0)
                    for line in lines:
                        f.write(line.strip() + "\n")
                    f.write(content)
                    files_modified += 1
else:
    print("Path is not a file...")
    # Otherwise, process all files in folder structure
    for root, dirs, files in os.walk(file_path):
        for file in files:
            total_files += 1
            if file.endswith("." + file_format):
                target_files += 1
                file_path = os.path.join(root, file)
                with open(file_path, "r+") as f:
                    content = f.read()
                    if remove_lines:
                        for line in lines:
                            if line + "\n" in content:
                                content = content.replace(line + "\n", "", 1)
                        files_modified += 1
                        f.seek(0)
                        f.write(content)
                        f.truncate()
                    else:
                        first_line = f.readline().strip()
                        if first_line not in lines:
                            f.seek(0)
                            for line in lines:
                                f.write(line.strip() + "\n")
                            f.write(content)
                            files_modified += 1

# Print stats
print(f"Total files: {total_files}")
print(f"Target files ({file_format}): {target_files}")
print(f"Files modified: {files_modified}")
print("Done!")
