import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("masters - Sheet1.csv")
print(df)



le_place = LabelEncoder()
df["Placed"] = le_place.fit_transform(df["Placed"])
le_gate = OrdinalEncoder(categories=[["MathScore","SciSccore","Good"]])
df["GATE_Score"] = le_gate.fit_transform(df[["GATE_Score"]])
le_masters = LabelEncoder()
df["Should_Do_Masters"] = le_masters.fit_transform(df["Should_Do_Masters"])
print(df)
x = df[["Placed","GATE_Score","Salary"]]
y = df["Should_Do_Masters"]

model = DecisionTreeClassifier()
model.fit(x,y)

data = [[0,2,0]]
predict_ans = model.predict(data)
print(predict_ans)
ins = le_masters.inverse_transform(predict_ans)
print(ins)