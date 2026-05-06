# Practical 3 Variables and Datatypes

roll_no = 205       # int
pi = 2.71828        # float
name = "Bob"        # str
is_pass = True      # bool
z = 5 + 4j          # complex
nothing = None      # NoneType

print(type(roll_no), type(pi), type(name))
print(type(is_pass), type(z), type(nothing))

# Multiple assignment
abc = 0             # all get same value
x, y, z = 50, 60, 70 # tuple unpacking
print(x, y, z)

# Type conversion (casting)
num_str = "42"               # str
num_int = int(num_str)       # str -> int
num_flt = float(num_int)     # int -> float
back_str = str(num_int)      # int -> str
print(num_int, num_flt, back_str)

# Dynamic typing demonstration
var = 99
print("Type:", type(var))
var = "now a string"
print("Type:", type(var))



