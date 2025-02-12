import pandas as pd

# Read data from a CSV file
df = pd.read_csv('rains.csv')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Display summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# Define the threshold value
threshold_value = 10  # Example threshold value

# Filter rows where a specific column value is greater than the threshold
filtered_df = df[df['agosto'] > threshold_value]
print("\nFiltered DataFrame (agosto > threshold_value):")
print(filtered_df)

# Group by a specific column and calculate the mean of another column
grouped_df = df.groupby('agosto')['diciembre'].mean()
print("\nGrouped DataFrame (mean of value_column by group_column):")
print(grouped_df)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data.csv', index=False)