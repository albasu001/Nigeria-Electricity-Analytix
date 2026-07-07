"""
Nigeria Electricity Analytics
Data Cleaning Script
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/electricity_raw.csv")

# Display basic information
print(df.info())
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove leading/trailing spaces from text columns
df["disco"] = df["disco"].str.strip()
df["region"] = df["region"].str.strip()

# Standardize text to uppercase
df["disco"] = df["disco"].str.upper()
df["region"] = df["region"].str.upper()

# Fill missing numeric values with the column median
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Save the cleaned dataset
df.to_csv("data/cleaned/electricity_cleaned.csv", index=False)

print("Data cleaning completed successfully.")
