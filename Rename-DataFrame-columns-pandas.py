import pandas as pd

#creat a dataframe
data={'A':[1,2,3],'B':[4,5,6]}
df=pd.DataFrame(data)

#rename columns
df.rename(columns={'A':'X','Y':'Z'}, inplace=True)
print(df)