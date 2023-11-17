import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Adding a new column
df['Salary'] = [50000, 60000, 75000]

# Displaying the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

# Performing some basic statistical analysis
print("\nSummary Statistics:")
print(df.describe())