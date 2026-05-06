"""Practical 12: Data Analysis with Pandas - Reading and Displaying CSV Files"""

import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Display the first few rows of the dataset
print(df.head())