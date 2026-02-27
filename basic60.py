from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("megh")
print(df)
print(df[["x"]])
print(df[["y"]])
plt.scatter(df.x,df.y)
plt.show()
reg = linear_model.LinearRegression()
reg.fit(df[["x"]],df[["y"]])
user = int(input("Enter the value of x"))
print(reg.predict([[user]]))