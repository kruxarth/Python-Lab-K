"""Practical 9 - Working with strings, lists, tuples and sets."""


def main() -> None:
    text = "Hello, Python World!"
    print(text.upper())
    print(text.lower())
    print("Length  :", len(text))
    print("Slice   :", text[7:13])
    print("Reverse :", text[::-1])
    print("Replace :", text.replace("Python", "Beautiful"))
    print("Split   :", text.split(", "))
    print("Find    :", text.find("Python"))

    values = [40, 10, 30, 50, 20]
    values.append(60)
    values.insert(2, 99)
    values.remove(99)
    values.sort()
    print("\nList    :", values)
    print("Sliced  :", values[1:4])
    print("Squares :", [number ** 2 for number in range(1, 6)])

    numbers = (1, 2, 3, 2, 4, 2)
    print("\nTuple   :", numbers)
    print("Count 2 :", numbers.count(2))
    print("Index 3 :", numbers.index(3))

    first, second, *rest = numbers
    print("Unpack  :", first, second, rest)

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print("\nUnion        :", set_a | set_b)
    print("Intersection :", set_a & set_b)
    print("Difference   :", set_a - set_b)
    print("Sym Diff     :", set_a ^ set_b)

    set_a.add(10)
    set_a.discard(1)
    print("Updated A    :", set_a)


if __name__ == "__main__":
    main()
