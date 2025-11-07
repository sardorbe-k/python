
# 1. Convert List to 1D Array

import numpy as np

# Original list
list1 = [12.23, 13.32, 100, 36.32]
print("Original List:", list1)

# Convert to NumPy array
array1 = np.array(list1)
print("One-dimensional NumPy array:", array1)

# 2. Create 3x3 Matrix (2–10)

matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

#  3. Null Vector (10) & Update Sixth Value

vector = np.zeros(10)
print("Original vector:", vector)

vector[5] = 11
print("Updated vector:", vector)

# 4. Array from 12 to 38

array = np.arange(12, 38)
print(array)

# 5. Convert Array to Float Type


arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array converted to float:", float_arr)

# 6. Celsius to Fahrenheit Conversion

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9/5) + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)

# 7. Append Values to Array

arr = np.array([10, 20, 30])
print("Original array:", arr)

new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append:", new_arr)


# 8. Array Statistical Functions (mean, median, std)     

arr = np.random.randint(1, 100, 10)  
print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

# 9. Find min and max

arr = np.random.rand(10, 10)  # 10x10 tasodifiy sonlar
print("Array:\n", arr)

print("Minimum value:", arr.min())
print("Maximum value:", arr.max())

# 10. Create 3x3x3 Array with Random Values

arr = np.random.random((3, 3, 3))
print(arr)
