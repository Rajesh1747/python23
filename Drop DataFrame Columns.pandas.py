import pandas as pd

#create a dataframe
data={'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]}
df = pd.DataFrame(data)

#Drop C column
df.drop(columns=['C'],inplace=True)
print(df)