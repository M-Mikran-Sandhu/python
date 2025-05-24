# Python File Operations: Text, CSV, and JSON

import os  # To check for file existence and remove files
import csv # For working with CSV files
import json # For working with JSON files

# -----------------------------------
# 1. WORKING WITH TEXT FILES (.txt)
# -----------------------------------
print("--- 1. Text File Operations ---")

# --- a. Opening and Writing to a Text File ---
# The `open()` function is used to open a file.
# 'w' mode: Opens the file for writing.
#           If the file exists, its content is overwritten.
#           If the file does not exist, it's created.
# Using `with open(...) as ...` is recommended because it automatically closes the file
# even if errors occur.
file_path_txt = "sample.txt"

print(f"\n[Text] Writing to {file_path_txt}...")
try:
    with open(file_path_txt, 'w') as file:
        # The `write()` method writes a string to the file.
        file.write("Hello, Python File I/O!\n")
        file.write("This is the second line.\n")
        # `writelines()` can write a list of strings. Each string should ideally end with '\n'.
        lines_to_write = ["Third line here.\n", "And a fourth one.\n"]
        file.writelines(lines_to_write)
    print(f"[Text] Successfully wrote to {file_path_txt}")
except IOError as e:
    print(f"[Text] Error writing to file: {e}")


# --- b. Reading from a Text File ---
# 'r' mode: Opens the file for reading (this is the default mode).
#           Raises an error if the file does not exist.
print(f"\n[Text] Reading from {file_path_txt}...")
try:
    with open(file_path_txt, 'r') as file:
        # `read()`: Reads the entire content of the file into a single string.
        print("\n[Text] Using file.read():")
        content = file.read()
        print(content)

    # Re-open to demonstrate other read methods (cursor is at the end after read())
    with open(file_path_txt, 'r') as file:
        # `readline()`: Reads a single line from the file, including the newline character.
        print("[Text] Using file.readline():")
        line1 = file.readline()
        print(f"Line 1: {line1.strip()}") # .strip() removes leading/trailing whitespace like '\n'
        line2 = file.readline()
        print(f"Line 2: {line2.strip()}")

    with open(file_path_txt, 'r') as file:
        # `readlines()`: Reads all lines from the file and returns them as a list of strings.
        # Each string in the list includes the newline character.
        print("\n[Text] Using file.readlines():")
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"Line {i+1}: {line.strip()}")
except FileNotFoundError:
    print(f"[Text] Error: The file {file_path_txt} was not found.")
except IOError as e:
    print(f"[Text] Error reading file: {e}")

# --- c. Appending to a Text File ---
# 'a' mode: Opens the file for appending.
#           New data is written to the end of the file.
#           If the file does not exist, it's created.
print(f"\n[Text] Appending to {file_path_txt}...")
try:
    with open(file_path_txt, 'a') as file:
        file.write("This line was appended.\n")
        file.write("Another appended line.\n")
    print(f"[Text] Successfully appended to {file_path_txt}")

    # Verify by reading again
    with open(file_path_txt, 'r') as file:
        print("\n[Text] Content after appending:")
        print(file.read())
except IOError as e:
    print(f"[Text] Error appending to file: {e}")

# --- d. Reading and Writing ('r+' mode) ---
# 'r+' mode: Opens the file for both reading and writing.
#            The file pointer is at the beginning. Overwrites existing content.
#            Raises an error if the file does not exist.
print(f"\n[Text] Using 'r+' mode with {file_path_txt}...")
try:
    with open(file_path_txt, 'r+') as file:
        print(f"[Text] Initial content (r+): {file.readline().strip()}") # Read the first line
        file.write("OVERWRITTEN FIRST LINE (r+)\n") # Overwrite from cursor position
        # Note: Be careful with r+ as it can be tricky to manage cursor position.
        # For complex operations, reading all, modifying, then writing all ('w') is often safer.
    print(f"[Text] Successfully used 'r+' on {file_path_txt}")

    with open(file_path_txt, 'r') as file:
        print("\n[Text] Content after 'r+' modification:")
        print(file.read())
except FileNotFoundError:
    print(f"[Text] Error: The file {file_path_txt} was not found for 'r+' operation.")
except IOError as e:
    print(f"[Text] Error with 'r+' operation: {e}")


# -----------------------------------
# 2. WORKING WITH CSV FILES (.csv)
# -----------------------------------
# CSV (Comma Separated Values) files are simple text files used to store tabular data.
print("\n\n--- 2. CSV File Operations ---")
file_path_csv = "sample.csv"

# --- a. Writing to a CSV File ---
# Data to write (list of lists, where each inner list is a row)
csv_data_to_write = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 24, "Los Angeles"],
    ["Charlie", 28, "Chicago"]
]

print(f"\n[CSV] Writing to {file_path_csv}...")
try:
    # `newline=''` is important to prevent blank rows in the CSV on some platforms.
    with open(file_path_csv, 'w', newline='') as csvfile:
        # `csv.writer` creates a writer object.
        csv_writer = csv.writer(csvfile)
        # `writerow()` writes a single row.
        # `writerows()` writes multiple rows from a list of lists.
        csv_writer.writerows(csv_data_to_write)
    print(f"[CSV] Successfully wrote to {file_path_csv}")
except IOError as e:
    print(f"[CSV] Error writing CSV file: {e}")

# --- b. Reading from a CSV File ---
print(f"\n[CSV] Reading from {file_path_csv}...")
try:
    with open(file_path_csv, 'r', newline='') as csvfile:
        # `csv.reader` creates a reader object.
        csv_reader = csv.reader(csvfile)
        # The reader object can be iterated over to get rows.
        # Each row is returned as a list of strings.
        print("[CSV] Contents:")
        for row in csv_reader:
            print(row) # Each 'row' is a list of strings
except FileNotFoundError:
    print(f"[CSV] Error: The file {file_path_csv} was not found.")
except IOError as e:
    print(f"[CSV] Error reading CSV file: {e}")

# --- c. Writing CSV data using csv.DictWriter (writing dictionaries) ---
csv_dict_data_to_write = [
    {'Name': 'David', 'Age': 35, 'City': 'Boston'},
    {'Name': 'Eve', 'Age': 22, 'City': 'Miami'}
]
# Define the fieldnames (column headers)
csv_fieldnames = ['Name', 'Age', 'City']
file_path_dict_csv = "sample_dict.csv"

print(f"\n[CSV] Writing dictionary data to {file_path_dict_csv}...")
try:
    with open(file_path_dict_csv, 'w', newline='') as csvfile:
        # `csv.DictWriter` needs the file object and a list of fieldnames.
        dict_writer = csv.DictWriter(csvfile, fieldnames=csv_fieldnames)
        # `writeheader()` writes the header row (fieldnames).
        dict_writer.writeheader()
        # `writerows()` writes all dictionaries in the list.
        dict_writer.writerows(csv_dict_data_to_write)
    print(f"[CSV] Successfully wrote dictionary data to {file_path_dict_csv}")
except IOError as e:
    print(f"[CSV] Error writing DictWriter CSV: {e}")

# --- d. Reading CSV data using csv.DictReader (reading into dictionaries) ---
print(f"\n[CSV] Reading data as dictionaries from {file_path_dict_csv}...")
try:
    with open(file_path_dict_csv, 'r', newline='') as csvfile:
        # `csv.DictReader` treats each row as a dictionary,
        # where keys are taken from the first (header) row.
        dict_reader = csv.DictReader(csvfile)
        print("[CSV] Contents (as dictionaries):")
        for row_dict in dict_reader:
            # Each 'row_dict' is an OrderedDict or dict (depending on Python version)
            print(dict(row_dict)) # Convert to regular dict for cleaner printing
            # print(f"Name: {row_dict['Name']}, Age: {row_dict['Age']}, City: {row_dict['City']}")
except FileNotFoundError:
    print(f"[CSV] Error: The file {file_path_dict_csv} was not found.")
except IOError as e:
    print(f"[CSV] Error reading DictReader CSV: {e}")


# -----------------------------------
# 3. WORKING WITH JSON FILES (.json)
# -----------------------------------
# JSON (JavaScript Object Notation) is a lightweight data-interchange format.
# It's easy for humans to read and write and easy for machines to parse and generate.
print("\n\n--- 3. JSON File Operations ---")
file_path_json = "sample.json"

# --- a. Writing to a JSON File (Serialization) ---
# Python dictionary to be stored as JSON
json_data_to_write = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "courses": [
        {"title": "History", "credits": 3},
        {"title": "Math", "credits": 4}
    ],
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    }
}

print(f"\n[JSON] Writing to {file_path_json}...")
try:
    with open(file_path_json, 'w') as jsonfile:
        # `json.dump()` serializes a Python dictionary into a JSON formatted string
        # and writes it to a file object.
        # `indent=4` makes the JSON file human-readable with pretty printing.
        json.dump(json_data_to_write, jsonfile, indent=4)
    print(f"[JSON] Successfully wrote to {file_path_json}")
except IOError as e:
    print(f"[JSON] Error writing JSON file: {e}")

# --- b. Reading from a JSON File (Deserialization) ---
print(f"\n[JSON] Reading from {file_path_json}...")
try:
    with open(file_path_json, 'r') as jsonfile:
        # `json.load()` deserializes a JSON formatted string from a file object
        # into a Python dictionary.
        loaded_data = json.load(jsonfile)
        print("[JSON] Contents (as Python dictionary):")
        print(loaded_data)
        print(f"[JSON] Name from loaded data: {loaded_data['name']}")
        print(f"[JSON] First course title: {loaded_data['courses'][0]['title']}")
except FileNotFoundError:
    print(f"[JSON] Error: The file {file_path_json} was not found.")
except json.JSONDecodeError as e:
    print(f"[JSON] Error decoding JSON: {e}")
except IOError as e:
    print(f"[JSON] Error reading JSON file: {e}")

# --- c. `dumps` and `loads` (string operations) ---
# `json.dumps()`: Serializes a Python object to a JSON formatted string (not to a file).
# `json.loads()`: Deserializes a JSON formatted string to a Python object.

print("\n[JSON] Using json.dumps() and json.loads()...")
python_dict = {"key": "value", "number": 42}
json_string = json.dumps(python_dict, indent=2) # Serialize to string
print(f"[JSON] Python dict serialized to JSON string:\n{json_string}")

reloaded_python_dict = json.loads(json_string) # Deserialize from string
print(f"[JSON] JSON string deserialized back to Python dict:\n{reloaded_python_dict}")
print(f"[JSON] Value from reloaded dict: {reloaded_python_dict['key']}")


# -----------------------------------
# 4. CLEANUP (Optional)
# -----------------------------------
# This section removes the files created by the script.
# You might want to comment this out if you want to inspect the files after running.
print("\n\n--- 4. Cleaning Up Sample Files ---")
files_to_remove = [file_path_txt, file_path_csv, file_path_dict_csv, file_path_json]
for f_path in files_to_remove:
    try:
        if os.path.exists(f_path):
            os.remove(f_path)
            print(f"[Cleanup] Successfully removed {f_path}")
        else:
            print(f"[Cleanup] File not found, no need to remove: {f_path}")
    except OSError as e:
        print(f"[Cleanup] Error removing file {f_path}: {e}")

print("\n--- File Operations Demonstration Complete ---")

# To run this file:
# 1. Save it as file_operations.py
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python file_operations.py
# The script will print its actions to the console and create/delete sample files.
