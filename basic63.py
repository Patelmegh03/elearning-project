import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load CSV file
df = pd.read_csv("sports_tryout.csv")
print(df)

# Encode the 'Selected' column (Yes/No)
le = LabelEncoder()
df["Selected"] = le.fit_transform(df["Selected"])  # Yes = 1, No = 0

# Features and Target
x = df[["Speed", "Strength", "Endurance"]]  # input columns
y = df["Selected"]                         # output column

# Train the Decision Tree
model = DecisionTreeClassifier()
model.fit(x, y)

# Make a prediction
# Example input: Speed=8, Strength=10, Endurance=7
data = [[8, 10, 7]]
pred = model.predict(data)
print(pred)

# Decode result: 1 = Yes, 0 = No
result = le.inverse_transform(pred)
print(result)