import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score

# Load CSV Data

try:
    df = pd.read_csv("student_performance.csv")
except FileNotFoundError:
    messagebox.showerror("File Error", "CSV file 'student_performance.csv' not found!")
    exit()

# Linear Regression Model

X = df[["Study_Hours", "Attendance", "Past_Score"]]
y = df["Final_Score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

reg_model = LinearRegression()
reg_model.fit(X_train, y_train)
accuracy = r2_score(y_test, reg_model.predict(X_test)) * 100  # Model accuracy %

# KMeans Clustering

kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Tkinter GUI

root = tk.Tk()
root.title("🎓 Student Performance Prediction")
root.geometry("600x550")
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

output_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green")
output_label.pack(pady=10)

# Functions

def predict_score():
    try:
        study = float(entry_hours.get())
        attend = float(entry_attendance.get())
        past = float(entry_past.get())

        if not (0 <= attend <= 100) or not (0 <= past <= 100) or not (0 <= study <= 24):
            raise ValueError

        features = pd.DataFrame([[study, attend, past]], columns=["Study_Hours", "Attendance", "Past_Score"])
        prediction = reg_model.predict(features)[0]

        if prediction < 60:
            category = "Low Performer"
        elif prediction < 80:
            category = "Average Performer"
        else:
            category = "High Performer"

        output_label.config(
            text=f"Predicted Final Score: {prediction:.2f}\n"
                 f"Category: {category}\n"
                 f"Model Accuracy: {accuracy:.2f}%"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in correct range!")

def show_clusters():
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

def clear_entries():
    entry_hours.delete(0, tk.END)
    entry_attendance.delete(0, tk.END)
    entry_past.delete(0, tk.END)
    output_label.config(text="")

# Buttons

tk.Button(root, text="Predict Score", font=("Arial", 12, "bold"), bg="lightblue", command=predict_score).pack(pady=5)
tk.Button(root, text="Show Clusters", font=("Arial", 12, "bold"), bg="lightgreen", command=show_clusters).pack(pady=5)
tk.Button(root, text="Show Regression Graph", font=("Arial", 12, "bold"), bg="orange", command=show_regression).pack(pady=5)
tk.Button(root, text="Clear Inputs", font=("Arial", 12, "bold"), bg="pink", command=clear_entries).pack(pady=5)

root.mainloop()
