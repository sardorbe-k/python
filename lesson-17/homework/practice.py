#  1
import pandas as pd

import numpy as np  # random qiymatlar uchun

# DataFrame yaratamiz
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Ustun nomlarini o‘zgartirish
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

print("\nRenamed DataFrame:")
print(df)

#  Dastlabki 3 qatorni chiqarish
print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

#  O‘rtacha yoshni topish
mean_age = df['age'].mean()
print("\nMean age of individuals:", mean_age)

#  Faqat 'first_name' va 'City' ustunlarini chiqarish
print("\nSelected columns (first_name and City):")
print(df[['first_name', 'City']])

#  Tasodifiy 'Salary' ustuni qo‘shamiz
df['Salary'] = np.random.randint(4000, 8000, size=len(df))
print("\nDataFrame with Salary column:")
print(df)

#  Statistik ma’lumotlar (summary statistics)
print("\nSummary statistics:")
print(df.describe())




# 2 — Sales and Expenses

# Jadval yaratamiz
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

print("Sales and Expenses DataFrame:")
print(sales_and_expenses)

# Maksimal qiymatlar
print("\nMaximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

# Minimal qiymatlar
print("\nMinimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

# O‘rtacha qiymatlar
print("\nAverage Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())



# 3 — Expenses jadvali

# Jadval yaratamiz
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

print("Original Expenses DataFrame:")
print(expenses)

# 'Category' ustunini index qilib olamiz
expenses.set_index('Category', inplace=True)
print("\nDataFrame with Category as index:")
print(expenses)

# Har bir kategoriya uchun maksimal, minimal va o‘rtacha xarajatlar
print("\nMaximum expense for each category:")
print(expenses.max(axis=1))

print("\nMinimum expense for each category:")
print(expenses.min(axis=1))

print("\nAverage expense for each category:")
print(expenses.mean(axis=1))

