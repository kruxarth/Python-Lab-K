"""Practical 1 - Introduction to Python and its installation."""

import platform
import sys


def display_environment_info() -> None:
    print("===== Python Environment Info =====")
    print("Python Version :", sys.version)
    print("Python Path    :", sys.executable)
    print("Platform       :", platform.system(), platform.release())
    print("Architecture   :", platform.architecture()[0])
    print()
    print("Installation verified successfully!")


if __name__ == "__main__":
    display_environment_info()
