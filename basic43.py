import pandas as pd

#
data={"Name":["a","b","c","a","b"],"Subject":["maths","maths","maths","science","science"],"Marks":[100,95,98,96,92]}
df=pd.DataFrame(data)
print(df)
p=df.pivot_table