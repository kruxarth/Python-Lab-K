import platform
import sys


def print_python_installation_info() -> None:
	print("Python Version:", sys.version)
	print("Python Path:", sys.executable)
	print("Platform:", platform.system(), platform.release())
	print("Architecture:", platform.architecture()[0])
	print("Installation verified successfully.")


if __name__ == "__main__":
	print_python_installation_info()
