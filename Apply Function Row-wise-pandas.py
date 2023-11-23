import pandas as pd

#creat a dataframe 
data= {'A':[4,5,6],'B':[7,8,9]}
df=pd.DataFrame(data)

#apply a function to each row
def sum_row(row):
    return row ['A'] +row['B']