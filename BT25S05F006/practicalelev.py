try:
    num = input("Enter mobile number: ")

    # check if input contains only digits
    if not num.isdigit():
        raise ValueError

    # check length
    if len(num) != 10:
        print("Invalid mobile number. It must contain exactly 10 digits.")
    else:
        print("Valid mobile number.")

except ValueError:
    print("Error: Please enter only numeric digits.")

finally:
    print("Program execution completed.")