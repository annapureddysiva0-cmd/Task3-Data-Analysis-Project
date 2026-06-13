# ==========================================
# IMPORT PANDAS
# ==========================================

import pandas as pd


# ==========================================
# LOAD CSV FILE
# ==========================================

df = pd.read_csv("sales_data.csv")

print("\n========== ORIGINAL DATA ==========\n")

print(df)


# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========\n")

print(df.isnull().sum())


# ==========================================
# REMOVE DUPLICATES
# ==========================================

df = df.drop_duplicates()


# ==========================================
# CREATE TOTAL SALES COLUMN
# ==========================================

df['Total_Sales'] = df['Price'] * df['Quantity']

print("\n========== DATA WITH TOTAL SALES ==========\n")

print(df)


# ==========================================
# FILTER ELECTRONICS PRODUCTS
# ==========================================

electronics = df[df['Category'] == 'Electronics']

print("\n========== ELECTRONICS PRODUCTS ==========\n")

print(electronics)


# ==========================================
# GROUP DATA BY CATEGORY
# ==========================================

grouped = df.groupby('Category')['Total_Sales'].sum()

print("\n========== TOTAL SALES BY CATEGORY ==========\n")

print(grouped)


# ==========================================
# SUMMARY STATISTICS
# ==========================================

print("\n========== SUMMARY STATISTICS ==========\n")

print(df.describe())


# ==========================================
# HIGHEST SALES PRODUCT
# ==========================================

highest_sales = df.loc[df['Total_Sales'].idxmax()]

print("\n========== HIGHEST SALES PRODUCT ==========\n")

print(highest_sales)


# ==========================================
# CITY-WISE SALES
# ==========================================

city_sales = df.groupby('City')['Total_Sales'].sum()

print("\n========== CITY-WISE SALES ==========\n")

print(city_sales)


print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")