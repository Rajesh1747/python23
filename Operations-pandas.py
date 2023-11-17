import pandas as pd

# Create a time series DataFrame
dates = pd.date_range('2023-01-01', periods=5)
df = pd.DataFrame({'Date': dates, 'Value': [1, 2, 3, 4, 5]})
print(df)