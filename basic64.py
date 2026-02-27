import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("moviedataset (1).csv")
print(df)

Le = LabelEncoder()
df["genre"] = Le.fit_transform(df["genre"])
x = df.drop("genre",axis=1)
y = df["genre"]

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=45)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

kclassifier = KNeighborsClassifier(n_neighbors=3)
kclassifier.fit(x_train_scaled,y_train)

prediction = kclassifier.predict(x_test_scaled)
print(Le.inverse_transform(prediction))
accuracy = accuracy_score(y_test,prediction)
print(accuracy)

new_data = [[40,4.2]]
new_data_scaled = scaler.transform(new_data)
new_prediction = kclassifier.predict(new_data_scaled)
print(Le.inverse_transform(new_prediction))