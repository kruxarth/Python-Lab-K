"""Practical 12 - Read and display a CSV dataset using pandas."""

from pathlib import Path

import pandas as pd


def main() -> None:
    csv_path = Path(__file__).with_name("students.csv")
    data_frame = pd.read_csv(csv_path, skipinitialspace=True)
    data_frame.columns = data_frame.columns.str.strip()
    print(data_frame.head())


if __name__ == "__main__":
    main()
