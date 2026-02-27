import pandas as pd
import numpy as np

data= pd.DataFrame([["x","y","z"],
                    ["d","e","f"],
                    ["g","h","i"]],
                    columns=["a","b","c"],index=[1,2,3])
print(data)

empdata=np.array([[8000,10000,18000],[15000,18000,25000]])

data1=pd.DataFrame(empdata,columns=[2020,2021,2022],index=["RAMESH","MAHESH"])
print(data1)

data1["2023"]=data1[2022]+data1[2022]*30/100
print(data1)

data1["TOTAL_2020_2021"]=data1[2020]+data1[2021]
print(data1)

data1["TOTAL_SALARY"]=data1[2020]+data1[2021]+data1[2022]
print(data1)

data1.drop("TOTAL_2020_2021",axis=1,inplace=True)
print(data1)

data1["deduct_2022"]=data1[2022]-1000
print(data1)

data1.drop("MAHESH",inplace=True)
print(data1)

data1.to_excel("add.xlsx", index=True)

