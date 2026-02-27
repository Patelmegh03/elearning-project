import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

# -------------------
# Dataset Creation
# -------------------
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 4, 6, 7, 2, 3, 8, 9, 10, 5, 6],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 92, 95, 50, 72, 88, 84, 55, 62, 91, 94, 96, 78, 82],
    "Past_Score": [55, 60, 62, 68, 72, 75, 80, 85, 90, 45, 64, 78, 82, 50, 58, 84, 88, 92, 70, 74],
    "Final_Score": [58, 62, 65, 70, 75, 78, 83, 87, 92, 48, 66, 80, 85, 52, 60, 86, 90, 94, 72, 76]
}
df = pd.DataFrame(data)

# Supervised model (Linear Regression)
X = df[["Study_Hours", "Attendance", "Past_Score"]]
y = df["Final_Score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Unsupervised model (KMeans)
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# -------------------
# Tkinter GUI
# -------------------
root = tk.Tk()
root.title("🎓 Student Performance Prediction")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Title Label
tk.Label(root, text="Student Performance Prediction", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="blue").pack(pady=10)

# Input Frame
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

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green")
output_label.pack(pady=10)

# -------------------
# Functions
# -------------------
def predict_score():
    try:
        study = float(entry_hours.get())
        attend = float(entry_attendance.get())
        past = float(entry_past.get())

        features = np.array([[study, attend, past]])
        prediction = reg_model.predict(features)[0]

        # Categorize performance
        if prediction < 60:
            category = "Low Performer"
        elif 60 <= prediction < 80:
            category = "Average Performer"
        else:
            category = "High Performer"

        output_label.config(text=f"Predicted Final Score: {prediction:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def show_clusters():
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x="Study_Hours", y="Final_Score", hue="Cluster", data=df, palette="deep")
    plt.title("Student Clusters Based on Performance")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Score")

    # Embed plot in Tkinter
    cluster_window = tk.Toplevel(root)
    cluster_window.title("Clusters")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=cluster_window)
    canvas.get_tk_widget().pack()
    canvas.draw()

def show_regression():
    plt.figure(figsize=(6, 4))
    sns.regplot(x="Study_Hours", y="Final_Score", data=df, ci=None, line_kws={"color": "red"})
    plt.title("Study Hours vs Final Score (Regression Line)")
    plt.xlabel("Study Hours")
    plt.ylabel("Final Score")

    reg_window = tk.Toplevel(root)
    reg_window.title("Regression Graph")
    canvas = FigureCanvasTkAgg(plt.gcf(), master=reg_window)
    canvas.get_tk_widget().pack()
    canvas.draw()

# -------------------
# Buttons
# -------------------
btn_predict = tk.Button(root, text="Predict Score", font=("Arial", 12, "bold"), bg="lightblue", command=predict_score)
btn_predict.pack(pady=5)

btn_cluster = tk.Button(root, text="Show Clusters", font=("Arial", 12, "bold"), bg="lightgreen", command=show_clusters)
btn_cluster.pack(pady=5)

btn_graph = tk.Button(root, text="Show Regression Graph", font=("Arial", 12, "bold"), bg="orange", command=show_regression)
btn_graph.pack(pady=5)

root.mainloop()