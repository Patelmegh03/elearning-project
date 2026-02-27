import pandas as pd
df=pd.read_csv("customer.csv")
print(df)

#find null value
print("null value",df.isnull().sum())

#tail and head
print("head\n",df.head())
print("tail\n",df.tail())
