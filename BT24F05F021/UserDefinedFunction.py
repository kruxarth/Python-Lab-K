
def greet_user(name):
    """This function greets the person passed in as a parameter"""
    print(f"Hello, {name}! Welcome to Python programming.")

def calculate_area(length, width):
    area = length * width
    return area

def power(base, exponent=2):
    return base ** exponent

greet_user("Alice")

room_area = calculate_area(15, 10)
print(f"The area is: {room_area} sq. units")

print(f"Square of 5: {power(5)}")     
print(f"Cube of 5: {power(5, 3)}")    