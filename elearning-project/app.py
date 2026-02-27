from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
import re

app = Flask(__name__)
app.secret_key = os.urandom(24)

# ------------------------
# Database Configuration
# ------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ------------------------
# Database Model
# ------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Create DB
with app.app_context():
    db.create_all()

# ------------------------
# Login Required Decorator
# ------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

# ------------------------
# Home Page
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------
# Register
# ------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        # Validation
        if len(username) < 4:
            flash("Username must be at least 4 characters.")
            return redirect(url_for("register"))

        if len(password) < 6:
            flash("Password must be at least 6 characters.")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("Username already exists.")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.")
        return redirect(url_for("login"))

    return render_template("register.html")

# ------------------------
# Login
# ------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Login successful!")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password.")
            return redirect(url_for("login"))

    return render_template("login.html")

# ------------------------
# Dashboard
# ------------------------
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=session["username"])

# ------------------------
# Courses
# ------------------------
@app.route("/courses")
@login_required
def courses():
    return render_template("courses.html")

# ------------------------
# Profile
# ------------------------
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = User.query.get(session["user_id"])

    if request.method == "POST":

        action = request.form.get("action")

        # Change Username
        if action == "username":
            new_username = request.form.get("new_username").strip()

            if len(new_username) < 4:
                flash("Username must be at least 4 characters.")
                return redirect(url_for("profile"))

            if User.query.filter_by(username=new_username).first():
                flash("Username already taken.")
                return redirect(url_for("profile"))

            user.username = new_username
            session["username"] = new_username
            db.session.commit()

            flash("Username updated successfully!")
            return redirect(url_for("profile"))

        # Change Password
        if action == "password":
            current_password = request.form.get("current_password")
            new_password = request.form.get("new_password")

            if not check_password_hash(user.password, current_password):
                flash("Current password incorrect.")
                return redirect(url_for("profile"))

            if len(new_password) < 6:
                flash("New password must be at least 6 characters.")
                return redirect(url_for("profile"))

            user.password = generate_password_hash(new_password)
            db.session.commit()

            flash("Password updated successfully!")
            return redirect(url_for("profile"))

    return render_template("profile.html", username=user.username)

# ------------------------
# Logout
# ------------------------
@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("login"))

# ------------------------
# Run App
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)