"""Practical 5 - Studying conditional statements in Python."""


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def calculate_grade(marks: int) -> str:
    if marks >= 90:
        return "O (Outstanding)"
    if marks >= 75:
        return "A+ (Excellent)"
    if marks >= 60:
        return "A (Very Good)"
    if marks >= 50:
        return "B (Good)"
    if marks >= 40:
        return "C (Pass)"
    return "F (Fail)"


def categorize_age(age: int) -> str:
    if age < 0:
        return "Invalid age entered!"
    if age < 13:
        return "Category: Child"
    if age < 18:
        return "Category: Teenager"
    if age < 60:
        return "Category: Adult"
    return "Category: Senior Citizen"


def main() -> None:
    marks = get_integer("Enter marks (0-100): ")
    print(f"Marks: {marks} -> Grade: {calculate_grade(marks)}")

    age = get_integer("\nEnter age: ")
    print(categorize_age(age))


if __name__ == "__main__":
    main()
