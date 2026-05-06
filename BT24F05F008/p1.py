# Practical 1 Introduction To Python And Its Installation

import sys
import platform

print("\n" + "="*50)
print("  PYTHON ENVIRONMENT INFORMATION")
print("="*50)
print(f"  Version:      {sys.version.split()[0]}")
print(f"  Executable:   {sys.executable}")
print(f"  OS:           {platform.system()} {platform.release()}")
print(f"  Architecture: {platform.architecture()[0]}")
print("="*50)
print("  ✓ Installation verified successfully!")
print("="*50 + "\n")









