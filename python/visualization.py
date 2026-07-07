"""
Nigeria Electricity Analytics
Data Visualization
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output directory if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("data/cleaned/electricity_cleaned.csv")

# Chart 1: Revenue by DisCo
plt.figure(figsize=(10, 6))
df.sort_values("revenue_billion_naira", ascending=False).plot(
    x="disco",
    y="revenue_billion_naira",
    kind="bar",
    legend=False
)
plt.title("Revenue by Electricity Distribution Company")
plt.xlabel("DisCo")
plt.ylabel("Revenue (₦ Billion)")
plt.tight_layout()
plt.savefig("images/revenue_by_disco.png")
plt.close()

# Chart 2: Metering Rate by DisCo
plt.figure(figsize=(10, 6))
df.plot(
    x="disco",
    y="metering_rate",
    kind="bar",
    legend=False
)
plt.title("Metering Rate by DisCo")
plt.xlabel("DisCo")
plt.ylabel("Metering Rate (%)")
plt.tight_layout()
plt.savefig("images/metering_rate.png")
plt.close()

print("Charts created successfully.")
