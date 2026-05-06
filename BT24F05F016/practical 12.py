import csv

csv_file = "employees.csv"

data = [
    ['Name', 'Age', 'Department', 'Salary'],
    ['Alice', 28, 'Engineering', 75000],
    ['Bob', 35, 'Marketing', 65000],
    ['Charlie', 26, 'Engineering', 70000],
]

with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

csv_file2 = "products.csv"

with open(csv_file2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product', 'Price', 'Quantity'])
    writer.writerow(['Laptop', 1200, 5])
    writer.writerow(['Mouse', 25, 50])
    writer.writerow(['Desk', 300, 10])

csv_file3 = "students.csv"
with open(csv_file3, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Name', 'Roll No', 'Grade'])
    writer.writerow(['Alice', 101, 'A'])
    writer.writerow(['Bob', 102, 'B'])

with open(csv_file2, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

fieldnames = ['Student', 'Math', 'English', 'Science']
students = [
    {'Student': 'Alice', 'Math': 95, 'English': 88, 'Science': 92},
    {'Student': 'Bob', 'Math': 87, 'English': 91, 'Science': 89},
    {'Student': 'Charlie', 'Math': 92, 'English': 85, 'Science': 88},
]

marks_file = "marks.csv"
with open(marks_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} - {row['Salary']}")

employees = []
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Age']) > 30:
            employees.append(row)

for emp in employees:
    print(emp)

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    salaries = [int(row['Salary']) for row in reader]
    print(f"Average: {sum(salaries)/len(salaries)}")

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for name, age, dept, sal in reader:
        print(f"{name}: {sal}")

csv_file_eng = "engineering.csv"
with open(csv_file_eng, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'Department', 'Salary'])
    writer.writeheader()
    with open(csv_file, 'r') as source:
        reader = csv.DictReader(source)
        for row in reader:
            if row['Department'] == 'Engineering':
                writer.writerow(row)

files = [csv_file, csv_file2, csv_file3, marks_file, csv_file_eng]
for f in files:
    try:
        __import__('os').remove(f)
    except:
        pass



# ==============================================================================
# PART 1: INTRODUCTION TO CSV FILES
# ==============================================================================

print("\nPART 1: INTRODUCTION TO CSV FILES")
print("-" * 70)

print("""
CSV (Comma-Separated Values) Format:
- Plain text format for tabular data
- Fields separated by commas or other delimiters
- One row per line
- Simple, widely supported, portable

Example CSV file:
    Name,Age,Department,Salary
    Alice,28,Engineering,75000
    Bob,35,Marketing,65000
    Charlie,26,Engineering,70000
    Diana,32,HR,60000

Advantages:
    ✓ Simple and readable
    ✓ Compatible with Excel and other tools
    ✓ Lightweight (smaller file size)
    ✓ Easy to parse and process
    ✓ Language independent
""")


# ==============================================================================
# PART 2: WRITING CSV FILES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 2: WRITING CSV FILES")
print("-" * 70)

# 2.1 Writing Simple CSV File
print("\n2.1 Writing Simple CSV File")

csv_file = "employees.csv"

# Method 1: Using csv.writer()
data = [
    ['Name', 'Age', 'Department', 'Salary'],
    ['Alice', 28, 'Engineering', 75000],
    ['Bob', 35, 'Marketing', 65000],
    ['Charlie', 26, 'Engineering', 70000],
    ['Diana', 32, 'HR', 60000],
    ['Eve', 29, 'Engineering', 72000]
]

try:
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"✓ CSV file '{csv_file}' created successfully")
except IOError as e:
    print(f"✗ Error creating file: {e}")


# 2.2 Writing CSV with writerow()
print("\n2.2 Writing CSV File Row by Row")

csv_file2 = "products.csv"

with open(csv_file2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product', 'Price', 'Quantity', 'Category'])
    writer.writerow(['Laptop', 1200, 5, 'Electronics'])
    writer.writerow(['Mouse', 25, 50, 'Electronics'])
    writer.writerow(['Desk', 300, 10, 'Furniture'])
    writer.writerow(['Chair', 150, 15, 'Furniture'])

print(f"✓ CSV file '{csv_file2}' created with writerow()")


# 2.3 Writing CSV with Different Delimiters
print("\n2.3 Writing CSV with Different Delimiters")

# Using semicolon as delimiter
csv_file3 = "students_semicolon.csv"
with open(csv_file3, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows([
        ['Student ID', 'Name', 'Math', 'English', 'Science'],
        ['001', 'Alice', 95, 88, 92],
        ['002', 'Bob', 87, 90, 85],
        ['003', 'Charlie', 92, 95, 90]
    ])

print(f"✓ Semicolon-delimited CSV created: {csv_file3}")

# Using pipe as delimiter
csv_file4 = "data_pipe.csv"
with open(csv_file4, 'w', newline='') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerows([
        ['ID', 'Name', 'Status'],
        [1, 'Active', 'Running'],
        [2, 'Inactive', 'Stopped']
    ])

print(f"✓ Pipe-delimited CSV created: {csv_file4}")


# ==============================================================================
# PART 3: READING CSV FILES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 3: READING CSV FILES")
print("-" * 70)

# 3.1 Reading CSV File with reader()
print("\n3.1 Reading CSV File with csv.reader()")

print(f"\nContent of '{csv_file}':")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row_num, row in enumerate(reader, 1):
        print(f"  Row {row_num}: {row}")


# 3.2 Reading Specific Columns
print("\n3.2 Reading Specific Columns")

print(f"\nReading Names and Salaries from '{csv_file}':")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Read header
    for row in reader:
        name = row[0]
        salary = row[3]
        print(f"  {name}: ${salary:,}")


# 3.3 Reading into a List
print("\n3.3 Reading All Data into a List")

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    all_rows = list(reader)

print(f"Total rows (including header): {len(all_rows)}")
print(f"Header: {all_rows[0]}")
print(f"First data row: {all_rows[1]}")


# ==============================================================================
# PART 4: READING CSV WITH DICTREADER
# ==============================================================================

print("\n" + "=" * 70)
print("PART 4: READING CSV WITH DICTREADER (Named Columns)")
print("-" * 70)

print(f"\nReading '{csv_file}' with DictReader (Name access):")

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  Name: {row['Name']}, Age: {row['Age']}, Department: {row['Department']}")


# ==============================================================================
# PART 5: WRITING CSV WITH DICTWRITER
# ==============================================================================

print("\n" + "=" * 70)
print("PART 5: WRITING CSV WITH DICTWRITER")
print("-" * 70)

print("\n5.1 Writing CSV with DictWriter")

csv_file5 = "courses.csv"
fieldnames = ['Course ID', 'Course Name', 'Instructor', 'Duration (hours)', 'Students']

courses = [
    {'Course ID': 'CS101', 'Course Name': 'Python Basics', 'Instructor': 'Dr. Smith', 'Duration (hours)': 40, 'Students': 25},
    {'Course ID': 'CS102', 'Course Name': 'Advanced Python', 'Instructor': 'Dr. Jones', 'Duration (hours)': 60, 'Students': 18},
    {'Course ID': 'CS103', 'Course Name': 'Data Science', 'Instructor': 'Dr. Brown', 'Duration (hours)': 80, 'Students': 22},
]

with open(csv_file5, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(courses)

print(f"✓ DictWriter CSV file created: {csv_file5}")

# Read it back
print(f"\nContent of '{csv_file5}':")
with open(csv_file5, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Course Name']} - Instructor: {row['Instructor']}")


# ==============================================================================
# PART 6: DATA MANIPULATION IN CSV
# ==============================================================================

print("\n" + "=" * 70)
print("PART 6: DATA MANIPULATION IN CSV")
print("-" * 70)

# 6.1 Filtering CSV Data
print("\n6.1 Filtering CSV Data")

print(f"Employees in Engineering Department:")
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Department'] == 'Engineering':
            print(f"  {row['Name']} - ${row['Salary']}")


# 6.2 Sorting CSV Data
print("\n6.2 Sorting CSV Data")

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    employees = list(reader)

# Sort by salary (highest to lowest)
employees_sorted = sorted(employees, key=lambda x: int(x['Salary']), reverse=True)

print(f"Employees by Salary (Highest to Lowest):")
for emp in employees_sorted:
    print(f"  {emp['Name']}: ${int(emp['Salary']):,}")


# 6.3 Filtering and Writing to New CSV
print("\n6.3 Filtering and Writing to New CSV")

csv_output = "engineering_only.csv"

with open(csv_file, 'r') as infile, open(csv_output, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        if row['Department'] == 'Engineering':
            writer.writerow(row)

print(f"✓ Filtered data written to '{csv_output}'")


# 6.4 Adding New Column to CSV
print("\n6.4 Adding New Column to CSV")

csv_bonus = "employees_with_bonus.csv"

with open(csv_file, 'r') as infile, open(csv_bonus, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Bonus']  # Add new field
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        salary = int(row['Salary'])
        row['Bonus'] = int(salary * 0.1)  # 10% bonus
        writer.writerow(row)

print(f"✓ New column 'Bonus' added: '{csv_bonus}'")
print(f"\nData with Bonus:")
with open(csv_bonus, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']}: Salary=${int(row['Salary']):,}, Bonus=${int(row['Bonus']):,}")


# ==============================================================================
# PART 7: CSV STATISTICS AND ANALYSIS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 7: CSV STATISTICS AND ANALYSIS")
print("-" * 70)

print("\n7.1 Calculating Statistics from CSV")

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    salaries = []
    departments = {}
    
    for row in reader:
        salary = int(row['Salary'])
        salaries.append(salary)
        dept = row['Department']
        departments[dept] = departments.get(dept, 0) + 1

print(f"Salary Statistics:")
print(f"  Total Employees: {len(salaries)}")
print(f"  Average Salary: ${sum(salaries) / len(salaries):,.0f}")
print(f"  Minimum Salary: ${min(salaries):,}")
print(f"  Maximum Salary: ${max(salaries):,}")

print(f"\nDepartment Count:")
for dept, count in departments.items():
    print(f"  {dept}: {count} employees")


# ==============================================================================
# PART 8: HANDLING CSV SPECIAL CHARACTERS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 8: HANDLING SPECIAL CHARACTERS IN CSV")
print("-" * 70)

print("\n8.1 CSV with Quoted Fields and Commas")

csv_special = "special_chars.csv"

data_special = [
    ['Name', 'Address', 'Comment'],
    ['Alice Johnson', '123 Main St, Apt 4B', 'Works on "Project X"'],
    ['Bob Smith', '456 Oak Ave, Suite 100', 'Quote: "Quality first"'],
    ['Charlie Brown', '789 Pine Rd, Building C', 'Uses: Python, Java, C++']
]

with open(csv_special, 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data_special)

print(f"✓ CSV with special characters created: '{csv_special}'")
print(f"\nContent:")
with open(csv_special, 'r') as f:
    print(f.read())


# ==============================================================================
# PART 9: ERROR HANDLING IN CSV OPERATIONS
# ==============================================================================

print("\n" + "=" * 70)
print("PART 9: ERROR HANDLING IN CSV OPERATIONS")
print("-" * 70)

print("\n9.1 Safe CSV Reading with Error Handling")

def safe_read_csv(filename):
    """Safely read CSV file with error handling."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        print(f"✓ Successfully read {len(data)} rows from '{filename}'")
        return data
    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
        return None
    except csv.Error as e:
        print(f"✗ CSV Error: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

data = safe_read_csv(csv_file)


# 9.2 Handling Different Encodings
print("\n9.2 Handling Different File Encodings")

def read_csv_with_encoding(filename, encoding='utf-8'):
    """Read CSV with specified encoding."""
    try:
        with open(filename, 'r', encoding=encoding) as f:
            reader = csv.reader(f)
            rows = list(reader)
        return rows
    except UnicodeDecodeError:
        print(f"✗ Failed to read with {encoding} encoding")
        return None
    except FileNotFoundError:
        print(f"✗ File not found: {filename}")
        return None

# Attempt to read with UTF-8 (most common)
rows = read_csv_with_encoding(csv_file, 'utf-8')
if rows:
    print(f"✓ Successfully read CSV with UTF-8 encoding")


# ==============================================================================
# PART 10: CSV ESCAPING AND QUOTING
# ==============================================================================

print("\n" + "=" * 70)
print("PART 10: CSV ESCAPING AND QUOTING OPTIONS")
print("-" * 70)

print("""
CSV Quoting Options:
  csv.QUOTE_MINIMAL     - Quote only when necessary
  csv.QUOTE_ALL         - Quote all fields
  csv.QUOTE_NONNUMERIC  - Quote all non-numeric fields
  csv.QUOTE_NONE        - Never quote
""")

print("\n10.1 Different Quoting Styles")

# Create sample data with special chars
sample_data = [
    ['Name', 'Email', 'Notes'],
    ['Alice', 'alice@example.com', 'Works on "Python" projects'],
    ['Bob', 'bob@example.com', 'Salary: $75,000']
]

# QUOTE_MINIMAL
with open('quote_minimal.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(sample_data)

# QUOTE_ALL
with open('quote_all.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(sample_data)

print(f"✓ QUOTE_MINIMAL: 'quote_minimal.csv'")
print(f"✓ QUOTE_ALL: 'quote_all.csv'")


# ==============================================================================
# PART 11: PRACTICAL EXAMPLES
# ==============================================================================

print("\n" + "=" * 70)
print("PART 11: PRACTICAL EXAMPLES")
print("-" * 70)

# Example 1: Sales Report Analysis
print("\n Example 1: Sales Report Creation and Analysis")

sales_file = "sales_report.csv"
sales_data = [
    ['Date', 'Product', 'Quantity', 'Price', 'Total'],
    ['2024-01-01', 'Laptop', 2, 1200, 2400],
    ['2024-01-02', 'Mouse', 5, 25, 125],
    ['2024-01-02', 'Laptop', 1, 1200, 1200],
    ['2024-01-03', 'Keyboard', 3, 80, 240],
    ['2024-01-03', 'Monitor', 2, 300, 600],
]

with open(sales_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sales_data)

# Analyze sales
with open(sales_file, 'r') as f:
    reader = csv.DictReader(f)
    total_revenue = sum(float(row['Total']) for row in reader)

with open(sales_file, 'r') as f:
    reader = csv.DictReader(f)
    product_sales = {}
    for row in reader:
        product = row['Product']
        total = float(row['Total'])
        product_sales[product] = product_sales.get(product, 0) + total

print(f"Sales Report Summary:")
print(f"  Total Revenue: ${total_revenue:,.2f}")
print(f"  Sales by Product:")
for product, amount in product_sales.items():
    print(f"    {product}: ${amount:,.2f}")


# Example 2: Grade Processing
print("\n Example 2: Grade Processing and Pass/Fail Assignment")

grades_file = "grades.csv"
grades_data = [
    ['Student', 'Math', 'English', 'Science'],
    ['Alice', 95, 88, 92],
    ['Bob', 45, 52, 48],
    ['Charlie', 78, 82, 75],
    ['Diana', 92, 95, 90],
]

with open(grades_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(grades_data)

# Process grades and add pass/fail
processed_file = "grades_processed.csv"

with open(grades_file, 'r') as infile, open(processed_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Average', 'Status']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in reader:
        math = int(row['Math'])
        english = int(row['English'])
        science = int(row['Science'])
        avg = (math + english + science) / 3
        
        row['Average'] = f"{avg:.1f}"
        row['Status'] = 'PASS' if avg >= 50 else 'FAIL'
        writer.writerow(row)

print(f"Processed Grades:")
with open(processed_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Student']}: Avg={row['Average']}, {row['Status']}")


# Example 3: Merging Two CSV Files
print("\n Example 3: Merging Multiple CSV Files")

# Create two separate CSV files
partners_file = "partners.csv"
with open(partners_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([
        ['Name', 'Department', 'Salary'],
        ['Frank', 'Finance', 80000],
        ['Grace', 'Legal', 85000],
    ])

# Merge with existing employees
merged_file = "all_staff.csv"

all_data = []

# Read first file
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    all_data.extend(list(reader))

# Read second file
with open(partners_file, 'r') as f:
    reader = csv.DictReader(f)
    all_data.extend(list(reader))

# Write merged file
if all_data:
    with open(merged_file, 'w', newline='') as f:
        fieldnames = all_data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
    
    print(f"✓ Merged {len(all_data)} records into '{merged_file}'")


# ==============================================================================
# PART 12: CSV CLEANUP
# ==============================================================================

print("\n" + "=" * 70)
print("CLEANUP - REMOVING TEST CSV FILES")
print("-" * 70)

csv_files = [
    'employees.csv', 'products.csv',
    'students_semicolon.csv', 'data_pipe.csv',
    'courses.csv', 'engineering_only.csv',
    'employees_with_bonus.csv', 'special_chars.csv',
    'quote_minimal.csv', 'quote_all.csv',
    'sales_report.csv', 'grades.csv', 'grades_processed.csv',
    'partners.csv', 'all_staff.csv'
]

for csv_file in csv_files:
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print(f"✓ Deleted: {csv_file}")

print("\n" + "=" * 70)
print("END OF PRACTICAL 12: CSV FILE OPERATIONS")
print("=" * 70)
