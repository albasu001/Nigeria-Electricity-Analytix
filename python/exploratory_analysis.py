"""
Nigeria Electricity Analytics
Exploratory Data Analysis (EDA)
"""

import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned/electricity_cleaned.csv")

# Preview the dataset
print("\nFirst 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Top 5 DisCos by revenue
print("\nTop 5 DisCos by Revenue:")
print(
    df.sort_values("revenue_billion_naira", ascending=False)[
        ["disco", "revenue_billion_naira"]
    ].head()
)

# Average performance metrics
print("\nAverage Performance Metrics:")
print(
   df[
    [
        "metering_rate",
        "billing_efficiency",
        "collection_efficiency",
        "cdi_score",
    ]
].mean()
)

print("\nEDA completed successfully.")
