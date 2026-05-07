import csv

def write_students_data():
    students = [
        ['Name', 'Roll', 'Branch', 'Marks', 'Grade'],  # Header
        ['Alice', 101, 'CS', 85, 'A'],
        ['Bob', 102, 'IT', 90, 'O'],
        ['Charlie', 103, 'ENTC', 72, 'B'],
        ['Diana', 104, 'CS', 95, 'O'],
        ['Eve', 105, 'IT', 68, 'B']
    ]

    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(students)

    print("Student data written to result.csv")




def write_subjects_data():
    subjects = [
        {'Subject': 'Python', 'Code': 'CS301', 'Credits': 3},
        {'Subject': 'DBMS', 'Code': 'CS302', 'Credits': 4},
        {'Subject': 'Networks', 'Code': 'CS303', 'Credits': 3}
    ]

    with open('subjects.csv', 'w', newline='') as file:
        fields = ['Subject', 'Code', 'Credits']
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(subjects)

    print("Subjects data written to subjects.csv")


def append_student():
    new_student = ['Frank', 106, 'MECH', 88, 'A']

    with open('result.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_student)

    print("New student record appended.")


def read_csv():
    print("\nFinal CSV Content:\n")

    with open('result.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print(', '.join(str(x) for x in row))


if __name__ == "__main__":
    write_students_data()
    write_subjects_data()
    append_student()
    read_csv()