# ==============================
# ONLINE RETAIL DATA CLEANING
# ==============================

# Step 1: Import required libraries
import pandas as pd
import numpy as np

# Step 2: Load dataset (Excel file)
df = pd.read_excel("Online Retail.xlsx")

# Step 3: Basic data overview
print("Shape of dataset (rows, columns):", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nDataset info:\n")
df.info()

# Step 4: Check missing values
print("\nMissing values in each column:\n")
print(df.isnull().sum())

# Step 5: Remove rows with missing CustomerID (important for analysis)
df = df.dropna(subset=["CustomerID"])

# Step 6: Convert CustomerID to integer (clean format)
df["CustomerID"] = df["CustomerID"].astype(int)

# Step 7: Remove cancelled orders (Invoice starting with 'C')
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Step 8: Remove negative or zero quantities
df = df[df["Quantity"] > 0]

# Step 9: Remove negative or zero prices
df = df[df["UnitPrice"] > 0]

# Step 10: Create new column: Total Sales
df["TotalSales"] = df["Quantity"] * df["UnitPrice"]

# Step 11: Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Step 12: Extract useful time features
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day
df["Hour"] = df["InvoiceDate"].dt.hour

# Step 13: Check duplicates and remove them
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 14: Final dataset info
print("\nFinal dataset shape:", df.shape)
print("\nClean dataset preview:\n", df.head())

# Step 15: Save cleaned dataset
df.to_csv("Online_Retail_Cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
