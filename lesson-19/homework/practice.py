
import pandas as pd

# 1. Load dataset
sales = pd.read_csv("task/sales_data.csv")

# 2. Group by Category and calculate aggregates
category_stats = sales.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
).reset_index()

print("=== Category statistics ===")
print(category_stats)

# 3. Top-selling product in each category
top_products = (
    sales.groupby(["Category", "Product"])["Quantity"]
    .sum()
    .reset_index()
    .sort_values(["Category", "Quantity"], ascending=[True, False])
    .groupby("Category")
    .head(1)
)
print("\n=== Top-selling products ===")
print(top_products)

# 4. Date with highest total sales (Quantity * Price)
sales["Total"] = sales["Quantity"] * sales["Price"]
top_date = (
    sales.groupby("Date")["Total"]
    .sum()
    .reset_index()
    .sort_values("Total", ascending=False)
    .head(1)
)
print("\n=== Date with highest total sales ===")
print(top_date)

import pandas as pd

# 1. Load dataset
orders = pd.read_csv("task/customer_orders.csv")

# 2. Group by CustomerID and filter customers with >= 20 orders
customer_order_count = orders.groupby("CustomerID")["OrderID"].count().reset_index(name="OrderCount")
active_customers = customer_order_count[customer_order_count["OrderCount"] >= 20]
print("=== Customers with 20+ orders ===")
print(active_customers)

# 3. Customers with avg price > $120
avg_price_customers = orders.groupby("CustomerID")["Price"].mean().reset_index()
rich_customers = avg_price_customers[avg_price_customers["Price"] > 120]
print("\n=== Customers with average price > $120 ===")
print(rich_customers)

# 4. Total quantity and price for each product, filter quantity >= 5
product_stats = orders.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
).reset_index()

filtered_products = product_stats[product_stats["total_quantity"] >= 5]
print("\n=== Products with total quantity >= 5 ===")
print(filtered_products)


import sqlite3
import pandas as pd

conn = sqlite3.connect("population.db")
cols = pd.read_sql_query("PRAGMA table_info(population);", conn)
print(cols[["name"]])
conn.close()

salary_col = "salary"



import pandas as pd
import sqlite3
import numpy as np

# === 1. Ma'lumotlarni o‘qish ===
conn = sqlite3.connect("population.db")
population = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Ma'lumotlarni tekshirish
print("Jadval ustunlari:", population.columns.tolist())

# Maosh ustuni nomi
salary_col = "salary"

# === 2. Salary Band chegaralari ===
bins = [0, 200000, 400000, 600000, 800000, 1000000,
        1200000, 1400000, 1600000, 1800000, float("inf")]

labels = [
    "till $200,000",
    "$200,001 - $400,000",
    "$400,001 - $600,000",
    "$600,001 - $800,000",
    "$800,001 - $1,000,000",
    "$1,000,001 - $1,200,000",
    "$1,200,001 - $1,400,000",
    "$1,400,001 - $1,600,000",
    "$1,600,001 - $1,800,000",
    "$1,800,001 and over"
]

# === 3. Kategoriya ustuni yaratish ===
population["Salary Band"] = pd.cut(
    population[salary_col],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# === 4. Statistikani hisoblash ===
table = population.groupby("Salary Band")[salary_col].agg(
    ["count", "mean", "median"]
).reset_index()

total_pop = table["count"].sum()
table["Percentage"] = (table["count"] / total_pop * 100).round(2)

# === 5. Ustun nomlarini tartiblash ===
table.rename(columns={
    "mean": "Average Salary",
    "median": "Median Salary",
    "count": "Number of population"
}, inplace=True)

table = table[[
    "Salary Band",
    "Percentage",
    "Average Salary",
    "Median Salary",
    "Number of population"
]]

# === 6. Natijani chiqarish ===
print("\n=== Salary Band bo‘yicha tahlil natijalari ===")
print(table)

# === 7. Excel faylga yozish ===
table.to_excel("population_salary_analysis_result.xlsx", index=False)
print("\n✅ Natija 'population_salary_analysis_result.xlsx' fayliga yozildi.")

