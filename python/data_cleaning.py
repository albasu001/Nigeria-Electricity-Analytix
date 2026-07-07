"""
Nigeria Electricity Analytics
Data Cleaning Script
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/electricity_raw.csv")

# Rename columns to a standard format
df = df.rename(columns={
    "DisCo": "disco",
    "Registered Customers": "registered_customers",
    "Metering Rate (%)": "metering_rate",
    "Billing Efficiency (%)": "billing_efficiency",
    "Collection Efficiency (%)": "collection_efficiency",
    "Total Complaints": "total_complaints",
    "Revenue (₦ Billion)": "revenue_billion_naira",
    "CDI Score": "cdi_score",
    "Complaint Score": "complaint_score",
    "Meter Score": "meter_score",
    "Billing Score": "billing_score",
    "Collection Score": "collection_score"
})

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
