"""Practical 9: Data Structures - String, List, Tuple, and Set with Operations"""

# String manipulation
text = "Python"
print(text.upper())  # Convert to uppercase
print(text[0])       # Access first character

# List operations
data_list = [1, 2, 3]
data_list.append(4)  # Add element to list
print(data_list)

# Tuple - immutable sequence
data_tuple = (1, 2, 3)
print(data_tuple[1])  # Access element at index 1

# Set - unordered collection of unique elements
data_set = {1, 2, 3}
data_set.add(4)      # Add element to set
print(data_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)           # All unique elements
print("Intersection:", set_a & set_b)    # Common elements