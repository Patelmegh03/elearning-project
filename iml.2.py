import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

# Load CSV Data

try:
    df = pd.read_csv("student_performance.csv")
except FileNotFoundError:
    print("CSV file 'student_performance.csv' not found!")
    exit()

# Data Preprocessing

df.fillna(df.mean(), inplace=True)
df["Study_Hours"] = df["Study_Hours"].clip(0, 24)
df["Attendance"] = df["Attendance"].clip(0, 100)
df["Past_Score"] = df["Past_Score"].clip(0, 100)
df["Final_Score"] = df["Final_Score"].clip(0, 100)

# Features and target

X = df[["Study_Hours", "Attendance", "Past_Score"]]
y = df["Final_Score"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Supervised Learning - Linear Regression

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict on test set

y_pred = lr_model.predict(X_test)
accuracy = r2_score(y_test, y_pred) * 100
print(f"Linear Regression Model Accuracy (R²): {accuracy:.2f}%")

# Example prediction for a new student

new_student = pd.DataFrame([[8, 75, 90]], columns=["Study_Hours", "Attendance", "Past_Score"])
new_student_scaled = scaler.transform(new_student)
predicted_score = lr_model.predict(new_student_scaled)[0]

if predicted_score < 60:
    category = "Low Performer"
elif predicted_score < 80:
    category = "Average Performer"
else:
    category = "High Performer"

print(f"Predicted Final Score for new student: {predicted_score:.2f} | Category: {category}")

# Unsupervised Learning - KMeans

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)
print("\nPredictions for 5 students::\n", df[["Study_Hours","Attendance","Past_Score","Cluster"]].head())

# Clusters

plt.figure(figsize=(6,4))
sns.scatterplot(x="Study_Hours", y="Final_Score", hue="Cluster", data=df, palette="viridis")
plt.title("Student Clusters (KMeans)")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()

# Regression: Study Hours vs Final Score
plt.figure(figsize=(6,4))
sns.scatterplot(x="Study_Hours", y="Final_Score", data=df, color='blue', label='Actual')
sns.lineplot(x=df["Study_Hours"], y=lr_model.predict(X_scaled), color='red', label='Regression Line')
plt.title("Linear Regression: Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.legend()
plt.show()

# Attendance vs Final Score
plt.figure(figsize=(6,4))
sns.scatterplot(x="Attendance", y="Final_Score", data=df, color="purple")
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.show()

# Past Score vs Final Score
plt.figure(figsize=(6,4))
sns.scatterplot(x="Past_Score", y="Final_Score", data=df, color="brown")
plt.title("Past Score vs Final Score")
plt.xlabel("Past Score")
plt.ylabel("Final Score")
plt.show()
