# Practical 12 - Object Oriented Programming (OOP)

class Student:
    # Class attribute
    school_name = "ABC High School"

    # Constructor (Initializer)
    def __init__(self, name, roll, marks):
        self.name = name        # instance attribute
        self.roll = roll
        self.marks = marks

    # Instance method
    def display_info(self):
        print(f"Name: {self.name} | Roll: {self.roll} | Marks: {self.marks}")

    # Method with logic
    def get_result(self):
        return "Pass" if self.marks >= 40 else "Fail"

# Creating objects (instances)
s1 = Student("Alice", 101, 85)
s2 = Student("Bob", 102, 35)

# Accessing methods and attributes
print(f"School: {Student.school_name}")
s1.display_info()
print(f"Result: {s1.get_result()}")

print("-" * 20)

s2.display_info()
print(f"Result: {s2.get_result()}")

# Modifying attribute
s2.marks = 45
print(f"Updated {s2.name}'s marks to {s2.marks}")
print(f"New Result: {s2.get_result()}")

# --- Inheritance ---
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):            # Method Overriding
        print("Dog Barks!")

class Cat(Animal):
    def speak(self):
        print("Cat Meows!")

# Testing Inheritance
d = Dog()
c = Cat()
d.speak()
c.speak()