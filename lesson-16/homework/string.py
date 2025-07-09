import numpy as np

# 1. Convert List to 1D Array
print("1. Convert List to 1D Array")
lst = [12.23, 13.32, 100, 36.32]
array_1d = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", array_1d)
print()

# 2. Create 3x3 Matrix (2→10)
print("2. Create 3x3 Matrix (2 to 10)")
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3)
print()

# 3. Null Vector (10) & Update Sixth Value
print("3. Null Vector of size 10 and update sixth value to 11")
null_vector = np.zeros(10)
print("Before update:", null_vector)
null_vector[6] = 11
print("After update:", null_vector)
print()

# 4. Array from 12 to 38
print("4. Array from 12 to 38")
array_12_38 = np.arange(12, 38)
print(array_12_38)
print()

# 5. Convert Array to Float Type
print("5. Convert Array to Float Type")
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print("Original array:", arr)
print("Converted to float:", float_arr)
print()

# 6. Celsius to Fahrenheit Conversion
print("6. Celsius to Fahrenheit Conversion")
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9 / 5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
print()

# 7. Append Values to Array
print("7. Append Values to Array")
original = np.array([10, 20, 30])
appended = np.append(original, [40, 50, 60, 70, 80, 90])
print("Original array:", original)
print("After append:", appended)
print()

# 8. Array Statistical Functions
print("8. Statistical Functions (mean, median, std)")
random_arr = np.random.rand(10)
print("Array:", random_arr)
print("Mean:", np.mean(random_arr))
print("Median:", np.median(random_arr))
print("Standard Deviation:", np.std(random_arr))
print()

# 9. Find min and max in 10x10
print("9. Min and Max in 10x10 array")
arr_10x10 = np.random.rand(10, 10)
print("Min:", np.min(arr_10x10))
print("Max:", np.max(arr_10x10))
print()

# 10. Create 3x3x3 array with random values
print("10. 3x3x3 Array with random values")
arr_3x3x3 = np.random.rand(3, 3, 3)
print(arr_3x3x3)
