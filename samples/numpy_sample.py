import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D array:", arr)

# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", arr_2d)

# Perform element-wise operations
arr_squared = arr ** 2
print("Squared array:", arr_squared)

# Calculate the mean and standard deviation
mean = np.mean(arr)
std_dev = np.std(arr)
print("Mean:", mean)
print("Standard Deviation:", std_dev)