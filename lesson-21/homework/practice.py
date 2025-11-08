import pandas as pd
import matplotlib.pyplot as plt

# DataFrame
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# -----------------------------
# Exercise 1: Average grade for each student
# -----------------------------
df1['Average'] = df1[['Math','English','Science']].mean(axis=1)
print("=== Average Grade per Student ===")
print(df1[['Student_ID', 'Average']])

# -----------------------------
# Exercise 2: Student with highest average grade
# -----------------------------
top_student = df1.loc[df1['Average'].idxmax()]
print("\n=== Student with Highest Average ===")
print(top_student[['Student_ID','Average']])

# -----------------------------
# Exercise 3: Total marks obtained by each student
# -----------------------------
df1['Total'] = df1[['Math','English','Science']].sum(axis=1)
print("\n=== Total Marks per Student ===")
print(df1[['Student_ID','Total']])

# -----------------------------
# Exercise 4: Bar chart of average grades in each subject
# -----------------------------
subject_avg = df1[['Math','English','Science']].mean()
plt.figure(figsize=(8,5))
subject_avg.plot(kind='bar', color=['skyblue','orange','green'])
plt.title('Average Grades in Each Subject')
plt.ylabel('Average Marks')
plt.xlabel('Subjects')
plt.ylim(0,100)
plt.show()



# DataFrame
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

# -----------------------------
# Exercise 1: Total sales per product
# -----------------------------
total_sales = df2[['Product_A','Product_B','Product_C']].sum()
print("=== Total Sales per Product ===")
print(total_sales)

# -----------------------------
# Exercise 2: Date with highest total sales
# -----------------------------
df2['Total_Sales'] = df2[['Product_A','Product_B','Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("\n=== Date with Highest Total Sales ===")
print(max_sales_date)

# -----------------------------
# Exercise 3: Percentage change from previous day
# -----------------------------
pct_change = df2[['Product_A','Product_B','Product_C']].pct_change() * 100
pct_change = pct_change.round(2)  # Round to 2 decimal places
print("\n=== Percentage Change in Sales ===")
print(pct_change)

# -----------------------------
# Exercise 4: Line chart of sales trends
# -----------------------------
plt.figure(figsize=(10,6))
plt.plot(df2['Date'], df2['Product_A'], marker='o', label='Product_A')
plt.plot(df2['Date'], df2['Product_B'], marker='o', label='Product_B')
plt.plot(df2['Date'], df2['Product_C'], marker='o', label='Product_C')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




# DataFrame
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

# -----------------------------
# Exercise 1: Average salary per department
# -----------------------------
avg_salary = df3.groupby('Department')['Salary'].mean().reset_index()
print("=== Average Salary per Department ===")
print(avg_salary)

# -----------------------------
# Exercise 2: Employee with most experience
# -----------------------------
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\n=== Employee with Most Experience ===")
print(most_experienced[['Employee_ID','Name','Experience (Years)']])

# -----------------------------
# Exercise 3: Salary Increase (%) from minimum salary
# -----------------------------
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print("\n=== Salary Increase Percentage ===")
print(df3[['Employee_ID','Name','Salary','Salary Increase (%)']])

# -----------------------------
# Exercise 4: Bar chart - distribution of employees across departments
# -----------------------------
dept_counts = df3['Department'].value_counts()
plt.figure(figsize=(8,5))
dept_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Employees per Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.show()




# DataFrame
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

# -----------------------------
# Exercise 1: Total revenue
# -----------------------------
total_revenue = df4['Total_Price'].sum()
print("=== Total Revenue ===")
print(total_revenue)

# -----------------------------
# Exercise 2: Most ordered product
# -----------------------------
most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print("\n=== Most Ordered Product ===")
print(most_ordered_product)

# -----------------------------
# Exercise 3: Average quantity of products ordered
# -----------------------------
average_quantity = df4['Quantity'].mean()
print("\n=== Average Quantity Ordered ===")
print(round(average_quantity, 2))

# -----------------------------
# Exercise 4: Pie chart of sales distribution by product
# -----------------------------
product_sales = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(6,6))
plt.pie(product_sales, labels=product_sales.index, autopct='%1.1f%%', startangle=90, colors=['skyblue','orange','green'])
plt.title('Sales Distribution by Product')
plt.show()
