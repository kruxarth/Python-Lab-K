"""Practical 2 - Create a simple Hello World program using Python."""


def main() -> None:
    print("Hello, World!")
    print("Hello", "World", sep=" | ", end="!\n")

    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print(f"\nHello, {name}! You are {age} years old.")
    print("Welcome to Python Programming!")

    result = 5 + 3
    print("Result: %d" % result)
    print("Result: {}".format(result))
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
