import pandas as pd

# conversion into datafram
lst = [10,20,30,40]
a= pd.DataFrame(lst)
print(a)

tup = (1,2,3,4,5)
b= pd.DataFrame(tup)
print(b)

dict = {"a":[30],"b":[50],"c":[70]}
c = pd.DataFrame(dict)
print(c)

#creatinf DataFrame

data = pd.DataFrame([[10,20,30],[40,50,60],[70,80,90]])
print(data)

data1= pd.DataFrame([["rohit","bat",50],
                    ["bumrah","bowl",64],
                    ["jadeja","all",80]],
                    columns=["name","type","run"])
print(data1)

data2= {"name":["gill","rohit"],
                "type":["bat","all"],
                "run":[80,45]}
data4= pd.DataFrame(data2)
print(data4)
print(data4["run"][0])
print(data4["name"])

# job salary
jobframe = pd.DataFrame([[10000,15000,17000],
                         [25000,27000,29000]],
                        columns=[2020,2021,2022],
                        index=["abc","xyz"])
print(jobframe)

jobframe[2023] = jobframe[2022]+(15*jobframe[2022]/[100])
print(jobframe)





