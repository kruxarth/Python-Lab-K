# Practical 3 — Working With Variables and Datatypes in Python
# Aim: To study and implement variables and different data types in Python.

roll_no = 101        # int
pi      = 3.14159    # float
name    = "Alice"    # str
is_pass = True       # bool
z       = 2 + 3j     # complex
nothing = None       # NoneType

print(type(roll_no), type(pi),      type(name))
print(type(is_pass), type(z),       type(nothing))

# Multiple assignment
a = b = c = 0               # all get same value
x, y, z = 10, 20, 30        # tuple unpacking
print(x, y, z)

# Type conversion (casting)
num_str  = "25"
num_int  = int(num_str)      # str  → int
num_flt  = float(num_int)    # int  → float
back_str = str(num_int)      # int  → str
print(num_int, num_flt, back_str)

# Dynamic typing demonstration
var = 10
print("Type:", type(var))
var = "now a string"
print("Type:", type(var))
