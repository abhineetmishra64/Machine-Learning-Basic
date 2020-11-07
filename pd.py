import pandas as pd

df = pd.read_table("abc.txt",delim_whitespace=True, names=('A','B','C'))
print(df)

#using .csv file

data = pd.read_csv("abc.txt",delimiter='\t',header=None,index_col=False)
data.coloumn = ["a","b","c"]
print(data)