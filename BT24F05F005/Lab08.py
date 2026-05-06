"""Practical 8 - Creating user defined functions in Python."""


def area_rectangle(length: int, width: int) -> int:
    return length * width


def greet(name: str, message: str = "Hello") -> str:
    return f"{message}, {name}!"


def add_all(*numbers: int) -> None:
    print(f"Sum of {len(numbers)} numbers:", sum(numbers))


def student_profile(**info: str) -> None:
    print("\nStudent Profile:")
    for key, value in info.items():
        print(f"  {key:<12}: {value}")


def cube(value: int) -> int:
    return value ** 3


def is_even(value: int) -> bool:
    return value % 2 == 0


def factorial(number: int) -> int:
    if number <= 1:
        return 1
    return number * factorial(number - 1)


def main() -> None:
    print("Area:", area_rectangle(5, 3))
    print(greet("Adarsh"))
    print(greet("Subham sir", "Good Morning"))

    add_all(1, 2, 3)
    add_all(10, 20, 30, 40)

    student_profile(name="Alice", roll=101, grade="A")

    print("\nCube of 4:", cube(4))
    print("Is 7 even :", is_even(7))

    for number in range(1, 7):
        print(f"  {number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
