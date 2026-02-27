import pandas as pd
import matplotlib.pyplot as plt

from Graph.basic15 import months

data={"students":["Manan","Pradip","Vraj","Marmik","Tejas","Manav","Om"],
      "JoiningDate":["2023-12-01","2023-11-01","2023-09-01","2023-09-01","2023-08-01","2023-06-01","2023-06-01"]}
df=pd.DataFrame(data)
print(df)
df["JoiningDate"]=pd.to_datetime(df["JoiningDate"])
df["Month"]=df["JoiningDate"].dt.month
df["Day"]=df["JoiningDate"].dt.day_name()
print(df)

#graph

months_joining=df["Month"].value_counts().sort_index()
months_joining.plot(kind="bar",title="Graph")
plt.show()











