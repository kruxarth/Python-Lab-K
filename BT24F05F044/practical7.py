"""Practical 7 - Working with built-in functions in Python."""


def square(value: int) -> int:
    return value * value


def is_even(value: int) -> bool:
    return value % 2 == 0


def main() -> None:
    numbers = [5, 2, 9, 1, 7, 4, 8, 3, 6]

    print("abs(-7)  :", abs(-7))
    print("round    :", round(3.14159, 3))
    print("pow(2,10):", pow(2, 10))
    print("divmod   :", divmod(17, 5))

    print("max      :", max(numbers))
    print("min      :", min(numbers))
    print("sum      :", sum(numbers))
    print("sorted   :", sorted(numbers))
    print("reversed :", list(reversed(numbers)))

    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")

    scores = [85, 90, 78]
    for fruit, score in zip(fruits, scores):
        print(f"  {fruit}: {score}")

    print("Squares:", list(map(square, numbers)))
    print("Evens   :", list(filter(is_even, numbers)))
    print("any > 8:", any(value > 8 for value in numbers))
    print("all > 0:", all(value > 0 for value in numbers))


if __name__ == "__main__":
    main()
