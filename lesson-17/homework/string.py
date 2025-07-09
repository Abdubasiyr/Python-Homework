import pandas as pd
import numpy as np

# === Homework 1 ===
print("=== Homework 1 ===")

data1 = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data1)

# 1. Rename columns
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)

# 2. First 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# 3. Mean age
print("\nMean age:", df['age'].mean())

# 4. Select name and city columns
print("\nName and City columns:")
print(df[['first_name', 'city']])

# 5. Add random salary column
df['salary'] = np.random.randint(3000, 7000, size=len(df))
print("\nDataFrame with salary:")
print(df)

# 6. Summary statistics
print("\nSummary statistics:")
print(df.describe())

# === Homework 2 ===
print("\n\n=== Homework 2 ===")

data2 = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(data2)

# Max values
print("\nMax Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

# Min values
print("\nMin Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

# Average values
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

# === Homework 3 ===
print("\n\n=== Homework 3 ===")

data3 = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(data3)

# Set index to 'Category'
expenses.set_index('Category', inplace=True)

# Max expenses per category
print("\nMax expense for each category:")
print(expenses.max(axis=1))

# Min expenses per category
print("\nMin expense for each category:")
print(expenses.min(axis=1))

# Average expenses per category
print("\nAverage expense for each category:")
print(expenses.mean(axis=1))
