import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the mean age
mean_age = df['Age'].mean()
print("\nMean Age:", mean_age)

# Filter rows where age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Add a new column
df['Salary'] = [70000, 80000, 60000, 90000]
print("\nDataFrame with Salary column:")
print(df)