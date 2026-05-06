import csv


def read_csv_file(file_path: str) -> None:
	"""Read and print data from a CSV file using Python's csv module."""
	try:
		with open(file_path, mode="r", newline="", encoding="utf-8") as csv_file:
			reader = csv.reader(csv_file)

			# Read and print header row (first row) if present
			header = next(reader, None)
			if header:
				print("Columns:", header)
				print("-" * 40)

			# Print remaining rows
			for row_number, row in enumerate(reader, start=1):
				print(f"Row {row_number}: {row}")

	except FileNotFoundError:
		print(f"Error: File '{file_path}' not found.")
	except PermissionError:
		print(f"Error: Permission denied for '{file_path}'.")
	except csv.Error as error:
		print(f"CSV parsing error: {error}")


if __name__ == "__main__":
	# Change this to your CSV file path if needed
	csv_path = "sample.csv"
	read_csv_file(csv_path)
