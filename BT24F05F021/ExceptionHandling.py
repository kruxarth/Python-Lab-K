def safe_divide():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        
        result = numerator / denominator
        
    except ValueError:
        print("Error: Please enter valid integers only.")
    except ZeroDivisionError:
        print("Error: You cannot divide a number by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    else:
        print(f"Division successful! Result: {result}")
        
    finally:
        print("Execution of the division function is complete.")

safe_divide()