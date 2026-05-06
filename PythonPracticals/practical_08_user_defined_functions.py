def greet(name):
    print("Hello,", name)
greet("Madhuri")
greet("Aarti")
def add(a, b):
    return a + b
result = add(12, 8)
print("Student: Rohit | Sum:", result)
def is_even(n):
    if n % 2 == 0:
        return True
    return False
print("Student: Tejas")
print("Is 14 even?", is_even(14))
print("Is 7 even?", is_even(7))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Student: Reema")
print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))
def student_info(name, city="Pune", course="BCA"):
    print(f"Name: {name}, City: {city}, Course: {course}")
student_info("Madhuri")
student_info("Aarti", "Mumbai", "BSc")
