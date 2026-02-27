import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("customer.csv")
cols = df.iloc[:,2:4]
print(cols)

oe = OrdinalEncoder(categories=[["Poor","Average","Good"],["School","UG","PG"]])
oe1 = oe.fit_transform(cols)
oe_df = pd.DataFrame(oe1)
print(oe_df)
df = pd.concat([df,oe_df],axis=1)
print(df)
df.drop(["review","education"],axis=1,inplace=True)
df.columns = ["age","gender","purchased","reviews","education"]
print(df)