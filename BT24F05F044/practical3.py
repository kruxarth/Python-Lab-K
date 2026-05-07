"""Practical 3 - Working with variables and datatypes in Python."""


def main() -> None:
    roll_number = 101
    pi_value = 3.14159
    student_name = "Alice"
    is_passed = True
    complex_number = 2 + 3j
    nothing = None

    print(type(roll_number), type(pi_value), type(student_name))
    print(type(is_passed), type(complex_number), type(nothing))

    first = second = third = 0
    x_value, y_value, z_value = 10, 20, 30
    print(x_value, y_value, z_value)

    number_text = "25"
    number_int = int(number_text)
    number_float = float(number_int)
    back_to_text = str(number_int)
    print(number_int, number_float, back_to_text)

    value = 10
    print("Type:", type(value))
    value = "now a string"
    print("Type:", type(value))


if __name__ == "__main__":
    main()
