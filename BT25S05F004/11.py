try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age >= 18:
        print("You are eligible for voting.")
    else:
        print("You are not eligible for voting.")

except ValueError as e:
    print("Invalid input:", e)

finally:
    print("Thank you for using voting checker.")