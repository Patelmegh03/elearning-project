import pandas as pd
att = {
    "day": list(range(1,11)),
    "att": [90,52,45,68,97,78,85,25,45,65]
}
df = pd.DataFrame(att)
print(df)
df["3 day avg"]=df["att"].rolling(window=3).mean()
print(df)

p = {
    "name":["a",'b','c','a','b'],
    "sub":["maths","maths","maths","science","science"],
    "mark":[89,45,65,87,85]
}
df1 = pd.DataFrame(p)
pivot = df1.pivot_table(values="mark",columns="sub",index="name",aggfunc="mean")
print(pivot)