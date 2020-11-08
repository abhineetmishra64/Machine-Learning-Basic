import pandas as pd
ds=pd.read_csv("Income_data.csv")
print(ds)
df2=ds.set_index("State")

df3 = df2.loc["Alabama":"Arizona","2005":"2007"]
print("Value of df3")
print(df3)
df4 = df2.loc[:,"2008"]
print("Value at 2008")
print(df4)
m = df4.mean()
s = df4.sum()
print("Average of sales tax in 2008",m)
print("Total sales tax in 2008",s)
df5 = df2.loc["California",:]
print(df5)
df6 = df2.iloc[0:3,1:3]
print("Using iloc")
print(df6)