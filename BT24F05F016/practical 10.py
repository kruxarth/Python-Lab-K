import os

filename = "sample.txt"

file = open(filename, 'w')
file.write("Hello, Python File Handling!\n")
file.write("This is the second line.\n")
file.write("This is the third line.\n")
file.close()

file = open(filename, 'r')
content = file.read()
file.close()
print(content)

file = open(filename, 'r')
line1 = file.readline()
line2 = file.readline()
file.close()
print(line1.strip())
print(line2.strip())

file = open(filename, 'r')
lines = file.readlines()
file.close()
print(lines)

with open(filename, 'r') as file:
    content = file.read()
    print(content)

with open(filename, 'r') as f:
    for line in f:
        print(line.strip())

test_file = "test.txt"
with open(test_file, 'w') as f:
    f.write("First version\n")

with open(test_file, 'a') as f:
    f.write("Second line\n")
print("File operations completed")

with open(filename, 'r') as f:
    content = f.read()
    print("Read successful")

if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"File size: {file_size} bytes")

with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

files_to_delete = [filename, test_file]
for f in files_to_delete:
    if os.path.exists(f):
        os.remove(f)
        print(f"Deleted: {f}")

    for student in students:
        f.write(f"Name: {student['name']}, Age: {student['age']}, GPA: {student['gpa']}\n")

print(f"✓ Records written to '{records_file}'")
with open(records_file, 'r') as f:
    print(f"\n{f.read()}")


# ==============================================================================
# PART 5: ERROR HANDLING IN FILE OPERATIONS
# ==============================================================================

print("=" * 70)
print("PART 5: ERROR HANDLING IN FILE OPERATIONS")
print("-" * 70)

# 5.1 Handling FileNotFoundError
print("\n5.1 Handling FileNotFoundError")
try:
    with open("nonexistent.txt", 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("✗ Error: File not found!")
except IOError as e:
    print(f"✗ I/O Error: {e}")


# 5.2 Handling Multiple Errors
print("\n5.2 Handling Multiple Errors")
def safe_read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"✗ Permission denied to read '{filename}'.")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

result = safe_read_file("sample.txt")
if result:
    print(f"Successfully read: {result[:50]}...")


# ==============================================================================
# PART 6: FILE INFORMATION AND PROPERTIES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 6: FILE INFORMATION AND PROPERTIES")
print("-" * 70)

# 6.1 Getting File Information
print("\n6.1 Getting File Information")
if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    file_path = os.path.abspath(filename)
    is_file = os.path.isfile(filename)
    is_dir = os.path.isdir(filename)
    
    print(f"Filename: {filename}")
    print(f"Absolute Path: {file_path}")
    print(f"File Size: {file_size} bytes")
    print(f"Is File: {is_file}")
    print(f"Is Directory: {is_dir}")


# 6.2 Getting File Statistics
print("\n6.2 File Statistics")
import time
stat_info = os.stat(filename)
print(f"File Mode: {stat_info.st_mode}")
print(f"File Size: {stat_info.st_size} bytes")
print(f"Last Modified: {time.ctime(stat_info.st_mtime)}")
print(f"Last Accessed: {time.ctime(stat_info.st_atime)}")


# ==============================================================================
# PART 7: FILE OPERATIONS - RENAME, COPY, DELETE
# ==============================================================================

print("\n" + "=" * 70)
print("PART 7: FILE OPERATIONS - RENAME, COPY, DELETE")
print("-" * 70)

# 7.1 Renaming a File
print("\n7.1 Renaming a File")
old_name = "mode_test.txt"
new_name = "mode_test_renamed.txt"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"✓ File renamed from '{old_name}' to '{new_name}'")


# 7.2 Copying a File
print("\n7.2 Copying a File")
import shutil
source_file = "sample.txt"
copy_file = "sample_backup.txt"
if os.path.exists(source_file):
    shutil.copy(source_file, copy_file)
    print(f"✓ File copied from '{source_file}' to '{copy_file}'")


# 7.3 Deleting a File
print("\n7.3 Deleting a File")
file_to_delete = "sample_copy.txt"
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"✓ File '{file_to_delete}' deleted")


# 7.4 Deleting Files with Specific Pattern
print("\n7.4 File Listing (Directory Operations)")
print(f"Files in current directory:")
files = os.listdir('.')
python_files = [f for f in files if f.endswith('.py')]
txt_files = [f for f in files if f.endswith('.txt')]
print(f"  Python files (.py): {len(python_files)}")
print(f"  Text files (.txt): {len(txt_files)}")


# ==============================================================================
# PART 8: WORKING WITH DIRECTORIES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 8: WORKING WITH DIRECTORIES")
print("-" * 70)

# 8.1 Creating Directories
print("\n8.1 Creating Directories")
new_dir = "test_directory"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"✓ Directory '{new_dir}' created")

# Create nested directories
nested_dir = "test_directory/sub_folder/another_level"
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir)
    print(f"✓ Nested directory created: {nested_dir}")


# 8.2 Listing Directory Contents
print("\n8.2 Listing Directory Contents")
current_dir = "."
print(f"Contents of '{current_dir}':")
try:
    for item in os.listdir(current_dir):
        path = os.path.join(current_dir, item)
        if os.path.isfile(path):
            print(f"  [FILE] {item}")
        elif os.path.isdir(path):
            print(f"  [DIR]  {item}")
except Exception as e:
    print(f"Error listing directory: {e}")


# 8.3 Removing Directories
print("\n8.3 Removing Directories")
dir_to_remove = "test_directory"
if os.path.exists(dir_to_remove):
    shutil.rmtree(dir_to_remove)
    print(f"✓ Directory '{dir_to_remove}' and contents removed")


# ==============================================================================
# PART 9: PATHLIB - MODERN PATH OPERATIONS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 9: USING PATHLIB (MODERN APPROACH)")
print("-" * 70)

# 9.1 Using Path Object
print("\n9.1 Using Path Object")
p = Path(filename)
print(f"Path: {p}")
print(f"Name: {p.name}")
print(f"Stem: {p.stem}")
print(f"Suffix: {p.suffix}")
print(f"Parent: {p.parent}")
print(f"Exists: {p.exists()}")
print(f"Is File: {p.is_file()}")
print(f"Is Directory: {p.is_dir()}")


# 9.2 Reading and Writing with Path
print("\n9.2 Reading and Writing with Path")
p = Path("pathlib_test.txt")
p.write_text("Hello from pathlib!\nThis is line 2.")
content = p.read_text()
print(f"Content:\n{content}")


# ==============================================================================
# PART 10: WORKING WITH JSON FILES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 10: WORKING WITH JSON FILES")
print("-" * 70)

# 10.1 Writing JSON Data
print("\n10.1 Writing JSON Data")
json_file = "data.json"
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "gaming"],
    "scores": {
        "math": 95,
        "english": 87
    }
}

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)
print(f"✓ JSON data written to '{json_file}'")


# 10.2 Reading JSON Data
print("\n10.2 Reading JSON Data")
with open(json_file, 'r') as f:
    loaded_data = json.load(f)
    print(f"Loaded data: {loaded_data}")
    print(f"Name: {loaded_data['name']}")
    print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")


# ==============================================================================
# PART 11: WORKING WITH CSV FILES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 11: WORKING WITH CSV FILES")
print("-" * 70)

# 11.1 Writing CSV Data
print("\n11.1 Writing CSV Data")
csv_file = "students.csv"
students = [
    ["Name", "Age", "Grade"],
    ["Alice", "20", "A"],
    ["Bob", "21", "B"],
    ["Charlie", "19", "A+"]
]

with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(students)
print(f"✓ CSV data written to '{csv_file}'")


# 11.2 Reading CSV Data
print("\n11.2 Reading CSV Data")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    print("CSV Content:")
    for row in reader:
        print(f"  {row}")


# 11.3 Reading CSV as Dictionary
print("\n11.3 Reading CSV as Dictionary (DictReader)")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    print("CSV Content (as dictionaries):")
    for row in reader:
        print(f"  {dict(row)}")


# ==============================================================================
# PART 12: PRACTICAL EXAMPLES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 12: PRACTICAL EXAMPLES")
print("-" * 70)

# Example 1: Reading and Processing a File
print("\n Example 1: Word Count and Line Count")
def analyze_file(filepath):
    """Analyze file: count lines, words, characters."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            
            return {
                'lines': len([l for l in lines if l.strip()]),
                'words': len(words),
                'characters': len(content)
            }
    except FileNotFoundError:
        return None

stats = analyze_file(filename)
if stats:
    print(f"File: {filename}")
    print(f"  Lines: {stats['lines']}")
    print(f"  Words: {stats['words']}")
    print(f"  Characters: {stats['characters']}")


# Example 2: Appending Logs to a File
print("\n Example 2: Writing Log File")
log_file = "app.log"
import datetime

def log_message(message, log_file=log_file):
    """Append message to log file with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

log_message("Application started")
log_message("Processing data")
log_message("Application ended")

print(f"✓ Logged 3 messages to '{log_file}'")
with open(log_file, 'r') as f:
    print(f"Log contents:\n{f.read()}")


# Example 3: Backup File
print("\n Example 3: Creating File Backup")
def backup_file(source, backup_dir="backups"):
    """Create backup of file in a backup directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    filename = os.path.basename(source)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{backup_dir}/{filename[:-4]}_backup_{timestamp}{Path(source).suffix}"
    
    if os.path.exists(source):
        shutil.copy2(source, backup_name)
        print(f"✓ Backup created: {backup_name}")
        return backup_name
    return None

# Example 4: Search for Pattern in Files
print("\n Example 4: Search Pattern in File")
def search_in_file(filepath, pattern):
    """Find lines containing pattern."""
    matches = []
    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if pattern.lower() in line.lower():
                    matches.append((line_num, line.strip()))
    except Exception as e:
        print(f"Error: {e}")
    
    return matches

results = search_in_file(records_file, "Alice")
if results:
    print(f"Found {len(results)} match(es) for 'Alice' in {records_file}:")
    for line_num, content in results:
        print(f"  Line {line_num}: {content}")


# ==============================================================================
# CLEANUP
# ==============================================================================

print("\n" + "=" * 70)
print("CLEANING UP TEST FILES")
print("-" * 70)

# List of test files to clean up
test_files = [
    "sample.txt", "sample_backup.txt", "sample_copy.txt",
    "mode_test_renamed.txt", "data.txt", "records.txt",
    "data.json", "students.csv", "app.log",
    "pathlib_test.txt"
]

for file in test_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"✓ Deleted: {file}")

print("\n" + "=" * 70)
print("END OF PRACTICAL 10: FILE HANDLING")
print("=" * 70)
