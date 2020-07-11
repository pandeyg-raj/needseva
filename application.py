from flask import Flask, render_template, session, request, redirect
from helper import sendEmail

app = Flask(__name__)

app.secret_key="asdkirj"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("Register.html")
    else:
        name=request.form.get("user")
        session["user_id"]=name
        return redirect("/")

@app.route("/signout")
def signout():
    session.clear()
    return redirect("/")

@app.route("/signin", methods=["POST","GET"])
def signin():
    return render_template("signin.html")

@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        sendEmail( request.form.get("Qemail"),  request.form.get("query") )

    return render_template("thankyou.html")

@app.route("/test", methods=["POST","GET"])
def test():
    return render_template("selectCV.html")

@app.route("/customer", methods=["POST","GET"])
def customer():
    return render_template("customer.html")
