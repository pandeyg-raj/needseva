from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("Register.html")

@app.route("/signin", methods=["POST","GET"])
def signin():
    return render_template("signin.html")
