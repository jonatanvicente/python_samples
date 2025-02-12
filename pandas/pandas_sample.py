import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

# Filter rows where age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Add a new column
df['Age in 5 Years'] = df['Age'] + 5
print("\nDataFrame with 'Age in 5 Years' column:")
print(df)