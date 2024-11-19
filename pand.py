from unittest.mock import inplace
import pandas as pd
import numpy as np
pd.options.display.max_rows = 60
data={'calories':[100,200,300],
      'name':['kavi','kalai','none']}
p=pd.DataFrame(data,index=['day1','day2','day3'])
# print(p.loc['day1'])
var=pd.read_csv("data.csv")
df=pd.DataFrame(var)
st=df.std()
print(df)
print(st)
# print("To print first 5 datas")
# print(var.tail(5))
# print(("To print last 5 datas"))
# print(var.head(5))
# print("To print number of non-null charectors in the dataset")
# print(var.info())
s=pd.Series([10.5,20,30,40,50],index=['a','b','c','d','e'],name="Numbers")
# print(s.array)
# print(s.values)
# print(s.dtype)
# print(s.shape)
# print(s.nbytes)
# print(s.ndim)
# print(s.memory_usage())
# print(s.memory_usage(index=False))
# print(s.size)
# print(s.name)
# print(s.empty)
# df=var.median()
# print(pd.DataFrame(var))
# print(var['Duration'].fillna(10))
# var.loc[3,'Duration']=90
# for x in var.index:
#       if var.loc[x,"Duration"]>45:
#             var.loc[x,"Duration"]=45
s1=pd.Series([10,20,30])
s2=pd.Series([40,50,60])
print(s1.add(s2))
