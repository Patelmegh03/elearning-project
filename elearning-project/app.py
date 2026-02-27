from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud Based E-Learning Project is Live!"