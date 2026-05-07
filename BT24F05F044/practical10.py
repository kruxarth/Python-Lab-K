"""Practical 10 - File handling using with."""

from pathlib import Path


def main() -> None:
    file_path = Path(__file__).with_name("student.txt")

    with file_path.open("w", encoding="utf-8") as file_handle:
        file_handle.write("Name: Dnyaneshwari Pandhare\n")
        file_handle.write("Course: Computer Science and Engineering\n")
        file_handle.write("Year: 2nd Year\n")

    print("Data written successfully!\n")

    with file_path.open("r", encoding="utf-8") as file_handle:
        print("Reading File Content:\n")
        print(file_handle.read())

    with file_path.open("a", encoding="utf-8") as file_handle:
        file_handle.write("College: GECA\n")

    print("\nData appended successfully!\n")

    with file_path.open("r", encoding="utf-8") as file_handle:
        print("Updated File Content:\n")
        print(file_handle.read())


if __name__ == "__main__":
    main()
