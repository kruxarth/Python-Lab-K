# Practical 1 — Introduction To Python And Its Installation
# Aim: To study the basic introduction of Python and verify its installation.

import sys
import platform

print("===== Python Environment Info =====")
print("Python Version :", sys.version)
print("Python Path    :", sys.executable)
print("Platform       :", platform.system(), platform.release())
print("Architecture   :", platform.architecture()[0])
print("")
print("Installation verified successfully!")
