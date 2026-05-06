# Introduction + System Info Program (to show Python is installed and working)

import sys
import platform
import datetime

print("----- PYTHON INSTALLATION CHECK -----")

print("Hello! Python is successfully installed.\n")

# Display Python Version
print("Python Version:", sys.version)

# Display Platform Info
print("Platform:", platform.system())
print("Processor:", platform.processor())

# Current Date & Time
now = datetime.datetime.now()
print("Current Date and Time:", now)

# Simple calculation to verify working
a = 10
b = 20
print("\nTesting calculation:")
print("Addition of", a, "and", b, "is:", a + b)

print("\nPython is working correctly!")