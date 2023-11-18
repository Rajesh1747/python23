import pandas as pd 

#creat a data frame 
data={'A':[1,2,3],'B':[4,5,6]}
df=pd.DataFrame(data)

#set 'B' column as index
df.set_index('B',inplace=True)
print(df)