import pandas as pd

#create a dataframe
data= {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Reset index
df.reset_index(inplace=True)
print(df)