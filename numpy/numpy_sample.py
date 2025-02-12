import numpy as np
import pandas as pd

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D array:")
print(array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:")
print(array_2d)

# Basic operations
array_sum = array_1d + 10
print("\nArray after adding 10:")
print(array_sum)

# Advanced operations
array_product = np.dot(array_2d, array_2d.T)
print("\nDot product of 2D array with its transpose:")
print(array_product)

# Universal functions
array_sqrt = np.sqrt(array_1d)
print("\nSquare root of 1D array:")
print(array_sqrt)

# Import data from a CSV file, using only the first 10 columns
data = np.genfromtxt('films.csv', delimiter=',', skip_header=1, usecols=range(10))
print("\nData imported from CSV:")
print(data)

# Export data to a CSV file
np.savetxt('exported_data.csv', data, delimiter=',')

# Indexing and slicing data
sliced_data = data[1:3, 2:4]
print("\nSliced data (rows 1-2, columns 2-3):")
print(sliced_data)

# Pandas integration
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print("\nDataFrame created from NumPy array:")
print(df)

# Treatment of missing data
df.iloc[0, 0] = np.nan  # Introduce a missing value
print("\nDataFrame with missing value:")
print(df)

df_filled = df.fillna(df.mean())
print("\nDataFrame after filling missing values with column mean:")
print(df_filled)