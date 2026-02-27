import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from datetime import datetime

# Load CSV Data

try:
    df = pd.read_csv("student_performance.csv")
except FileNotFoundError:
    messagebox.showerror("File Error", "CSV file 'student_performance.csv' not found!")
    exit()

# Data Preprocessing

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Past_Score"] = df["Past_Score"].fillna(df["Past_Score"].mean())
df["Final_Score"] = df["Final_Score"].fillna(df["Final_Score"].mean())

df["Study_Hours"] = df["Study_Hours"].clip(0, 24)
df["Attendance"] = df["Attendance"].clip(0, 100)
df["Past_Score"] = df["Past_Score"].clip(0, 100)
df["Final_Score"] = df["Final_Score"].clip(0, 100)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[["Study_Hours", "Attendance", "Past_Score"]])
y = df["Final_Score"]

# Linear Regression Model

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)
accuracy = r2_score(y_test, reg_model.predict(X_test)) * 100

# KMeans Clustering

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Tkinter GUI

root = tk.Tk()
root.title("🎓 Student Performance Prediction")
root.geometry("650x650")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Student Performance Prediction", font=("Arial", 16, "bold"),
         bg="#f0f0f0", fg="blue").pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Study Hours:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5)
entry_hours = tk.Entry(frame, font=("Arial", 12))
entry_hours.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Attendance (%):", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
entry_attendance = tk.Entry(frame, font=("Arial", 12))
entry_attendance.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Past Score:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5)
entry_past = tk.Entry(frame, font=("Arial", 12))
entry_past.grid(row=2, column=1, padx=5, pady=5)

output_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green", justify="left")
output_label.pack(pady=10)

# Functions

def predict_score():
    try:
        study = float(entry_hours.get())
        attend = float(entry_attendance.get())
        past = float(entry_past.get())

        if not (0 <= attend <= 100) or not (0 <= past <= 100) or not (0 <= study <= 24):
            raise ValueError

        # Transform input using DataFrame with same column names to avoid warning
        features_scaled = scaler.transform(pd.DataFrame([[study, attend, past]], columns=["Study_Hours", "Attendance", "Past_Score"]))
        prediction = reg_model.predict(features_scaled)[0]

        if prediction < 60:
            category = "Low Performer"
            recommendation = ("💡 Recommendation:\n"
                              "- Increase study hours gradually.\n"
                              "- Improve attendance to above 75%.\n"
                              "- Review past lessons and practice more.\n")
        elif prediction < 80:
            category = "Average Performer"
            recommendation = ("💡 Recommendation:\n"
                              "- Keep consistent study schedule.\n"
                              "- Focus on weak topics.\n")
        else:
            category = "High Performer"
            recommendation = "🎉 Keep up the excellent work!"

        output_label.config(
            text=f"Predicted Final Score: {prediction:.2f}\n"
                 f"Category: {category}\n"
                 f"Model Accuracy: {accuracy:.2f}%\n\n"
                 f"{recommendation}"
        )

        save_prediction(study, attend, past, prediction, category)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in correct range!")

def save_prediction(study, attend, past, prediction, category):
    data = {
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Study_Hours": [study],
        "Attendance": [attend],
        "Past_Score": [past],
        "Predicted_Final_Score": [prediction],
        "Category": [category]
    }
    pred_df = pd.DataFrame(data)
    pred_df.to_csv("predictions_log.csv", mode="a", index=False,
                   header=not pd.io.common.file_exists("predictions_log.csv"))

def show_clusters():
    plt.close('all')
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="Study_Hours", y="Final_Score", hue="Cluster", data=df, palette="deep")
    plt.title("Student Clusters Based on Performance")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Score")
    win = tk.Toplevel(root)
    win.title("Clusters")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=win)
    canvas.get_tk_widget().pack()
    canvas.draw()

def show_regression():
    plt.close('all')
    plt.figure(figsize=(6, 4))
    sns.regplot(x="Study_Hours", y="Final_Score", data=df, ci=None, line_kws={"color": "red"})
    plt.title("Study Hours vs Final Score (Regression Line)")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Score")
    win = tk.Toplevel(root)
    win.title("Regression Graph")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=win)
    canvas.get_tk_widget().pack()
    canvas.draw()

def show_attendance_scatter():
    plt.close('all')
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="Attendance", y="Final_Score", data=df, color="purple")
    plt.title("Attendance vs Final Score")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Final Score")
    win = tk.Toplevel(root)
    win.title("Attendance Scatter Plot")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=win)
    canvas.get_tk_widget().pack()
    canvas.draw()

def show_past_score_scatter():
    plt.close('all')
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="Past_Score", y="Final_Score", data=df, color="brown")
    plt.title("Past Score vs Final Score")
    plt.xlabel("Past Score")
    plt.ylabel("Final Score")
    win = tk.Toplevel(root)
    win.title("Past Score Scatter Plot")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=win)
    canvas.get_tk_widget().pack()
    canvas.draw()


def clear_entries():
    entry_hours.delete(0, tk.END)
    entry_attendance.delete(0, tk.END)
    entry_past.delete(0, tk.END)
    output_label.config(text="")

# Buttons

tk.Button(root, text="Predict Score", font=("Arial", 12, "bold"), bg="lightblue", command=predict_score).pack(pady=5)
tk.Button(root, text="Show Clusters", font=("Arial", 12, "bold"), bg="lightgreen", command=show_clusters).pack(pady=5)
tk.Button(root, text="Show Regression Graph", font=("Arial", 12, "bold"), bg="orange", command=show_regression).pack(pady=5)
tk.Button(root, text="Attendance vs Final Score", font=("Arial", 12, "bold"), bg="violet", command=show_attendance_scatter).pack(pady=5)
tk.Button(root, text="Past Score vs Final Score", font=("Arial", 12, "bold"), bg="brown", fg="white", command=show_past_score_scatter).pack(pady=5)
tk.Button(root, text="Clear Inputs", font=("Arial", 12, "bold"), bg="pink", command=clear_entries).pack(pady=5)

root.mainloop()
