"""Practical 4 - Studying various types of operators in Python."""


def main() -> None:
    a, b = 10, 3

    print("Arithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
    print("Comparison :", a == b, a != b, a > b, a < b, a >= b, a <= b)

    x = 5
    x += 3
    print("x after +=3 :", x)
    x -= 2
    print("x after -=2 :", x)
    x **= 2
    print("x after **=2:", x)

    print("Logical:", (a > 5 and b < 5), (a < 5 or b < 5), not (a == b))
    print("Bitwise: &=", a & b, "|", a | b, "^=", a ^ b, "~a=", ~a, "<<", a << 1, ">>", a >> 1)

    list_one = [1, 2, 3]
    list_two = list_one
    list_three = [1, 2, 3]
    print(list_one is list_two)
    print(list_one is list_three)
    print(list_one is not list_three)


if __name__ == "__main__":
    main()
