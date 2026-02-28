from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = "secretkey"

# ---------------- DATABASE ----------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

with app.app_context():
    db.create_all()

# ---------------- LOGIN REQUIRED ----------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            return redirect(url_for("register"))

        new_user = User(
            username=username,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            return redirect(url_for("dashboard"))

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=session["username"])

# ---------------- COURSES ----------------
@app.route("/courses")
@login_required
def courses():
    folders = [
        "CLOUD COMPUTING",
        "FUNDAMENTAL OF IOT",
        "COMPUTER MAINTANENCE AND TROUBLESHOOTING",
        "BASICS OF INFORMATION SECURITY",
        "INTRODUCTION TO NO SQL"
    ]
    return render_template("course.html", folders=folders)

# ---------------- OPEN FOLDER ----------------
@app.route("/folder/<folder_name>")
@login_required
def open_folder(folder_name):

    # FULL correct static path
    folder_path = os.path.join(app.root_path, "static", folder_name)

    if not os.path.isdir(folder_path):
        return f"Folder {folder_name} not found"

    files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    return render_template(
        "cloud.html",
        folder_name=folder_name,
        files=files
    )

# ---------------- ADD COURSE ----------------
@app.route("/add_course")
@login_required
def add_course():
    return render_template("add_course.html")

# ---------------- PROFILE ----------------
@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)