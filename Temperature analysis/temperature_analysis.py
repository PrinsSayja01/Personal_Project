import pandas as pd

# 1. Load the dataset
try:
    df = pd.read_csv('weather.csv')
    print("Data loaded successfully.\n")
except FileNotFoundError:
    print("Error: 'weather.csv' not found. Please check the file path.")
    exit()

# 2. Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# 3. Basic Statistics
print("\nBasic Statistics:")
print(df.describe())

# 4. Mean and Median
print("\nMean values:")
print(df.mean(numeric_only=True))

print("\nMedian values:")
print(df.median(numeric_only=True))

# 5. Missing Values Check
print("\nMissing values in the dataset:")
print(df.isnull().sum())
