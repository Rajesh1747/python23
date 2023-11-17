import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Apply a function to each element
squared = df.applymap(lambda x: x ** 2)
print(squared)