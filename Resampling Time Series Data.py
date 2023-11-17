import pandas as pd
import numpy as np

# Create a time series DataFrame
dates = pd.date_range('2023-01-01', periods=10, freq='D')
df = pd.DataFrame({'Date': dates, 'Value': np.random.randn(10)})
print(df)

# Resample data to monthly frequency
monthly = df.resample('M', on='Date').mean()
print(monthly)
