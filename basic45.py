import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("customer.csv")
print(df)

label_encoder = LabelEncoder()
df["gender"] = label_encoder.fit(df["gender"])
print(df)



