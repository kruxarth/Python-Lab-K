"""Practical 11 - File handling with exception handling."""

from pathlib import Path


def main() -> None:
    try:
        filename = input("Enter file name: ").strip()
        if not filename:
            raise ValueError("File name cannot be empty.")

        file_path = Path(filename)
        with file_path.open("r", encoding="utf-8") as file_handle:
            print("\nFile Content:\n")
            print(file_handle.read())

    except FileNotFoundError:
        print("Error: File does not exist!")
    except ValueError as error:
        print("Error:", error)
    except Exception as error:
        print("Something went wrong:", error)
    finally:
        print("\nProgram executed.")


if __name__ == "__main__":
    main()
