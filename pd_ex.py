import pandas as pd
import numpy as np
#same process for dictionary
a = pd.read_csv("student.csv")
print(a)
data = np.array(['a','b','c','d'])
b = pd.Series(data)
print(b)
data1 = np.array(['a','b','c','d'])
c = pd.Series(data1, index=[101,102,103,104])
print(c)