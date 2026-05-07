"""Practical 6 - Studying various kinds of loops in Python."""


def main() -> None:
    print("Squares using for loop:", end=" ")
    for number in range(1, 6):
        print(number ** 2, end=" ")
    print()

    print("Fibonacci (while loop):")
    first, second, count = 0, 1, 8
    while count > 0:
        print(first, end=" ")
        first, second = second, first + second
        count -= 1
    print()

    print("\nMultiplication Table (3x3):")
    for row in range(1, 4):
        for column in range(1, 4):
            print(f"{row * column:3}", end="")
        print()

    print("\nSkip even, stop at 7:")
    for value in range(1, 10):
        if value % 2 == 0:
            continue
        if value == 7:
            break
        print(value, end=" ")
    print()

    numbers = [2, 4, 7, 10]
    for value in numbers:
        if value == 7:
            print("\n7 found in list!")
            break
    else:
        print("\n7 not found")


if __name__ == "__main__":
    main()
