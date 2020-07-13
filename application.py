from flask import Flask, render_template, session, request, redirect
from helper import sendEmail
from functools import wraps
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqldatabase import User, Recover, Details, Queries
from sqlalchemy import join
from sqlalchemy.sql import select
engine = create_engine('sqlite:///needseva.db', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)


app = Flask(__name__)

app.secret_key="asdkirj"

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/signin")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "GET":
        return render_template("Register.html")
    else:
        dbsession = Session()
        name = request.form.get("user")
        pwd = request.form.get("pass")
        obj = User(name,pwd);
        dbsession.add(obj)
        session["user_id"]=name

        question = request.form.get("recoverpass")
        answer = request.form.get("ans")
        obj1 = Recover(name,question,answer);
        dbsession.add(obj1)

        fname = request.form.get("fname")
        lname = request.form.get("lname")
        address = request.form.get("add")
        email = request.form.get("email")
        phone = request.form.get("phNo")
        zip = request.form.get("zip")
        obj2 = Details(name, fname, lname, address, zip, email, phone)
        dbsession.add(obj2)

        dbsession.commit()
        dbsession.close()
        return render_template("selectCV.html")

@app.route("/signout")
@login_required
def signout():
    session.clear()
    return redirect("/")

@app.route("/signin", methods=["POST","GET"])
def signin():
    if request.method == "GET":
        if session.get("user_id") is None:
            return render_template("signin.html")
        else:
            return redirect("/")
    else:
        dbsession = Session()
        username = request.form.get("username")
        password = request.form.get("password")

        exists = dbsession.query(User).filter(User.username == username).filter(User.hash == password).scalar()

        if exists is not None:
            dbsession.close()
            session["user_id"]=username
            return render_template("selectCV.html")

        dbsession.close()
        return render_template("invalid.html")



@app.route("/contact", methods=["POST","GET"])
@login_required
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        body = 'customer email: ' + request.form.get("Qemail") + '\n Customer request: ' + request.form.get("query") 
        sendEmail( "patelg.hima@gmail.com", "NeedSeva Customer",  body)
        return render_template("common.html", value = "Thank You for contacting us!")

@app.route("/test", methods=["POST","GET"])
@login_required
def test():
    return render_template("selectCV.html")

@app.route("/vol")
@login_required
def vol():
    dbsession = Session()
    #print("data start")
    results = dbsession.query(Details,Queries).filter( Details.username == Queries.username).all()
    return render_template("customerlisting.html",DATA = results)

@app.route("/customer", methods=["POST","GET"])
@login_required
def customer():
    if request.method == "GET":
        dbsession = Session()
        user = session["user_id"]

        exists = dbsession.query(Queries.username).filter_by( username = user ).scalar()
        
        #results = dbsession.query(Queries).filter(Queries.username == user)
        if exists is not None:
            results = dbsession.query(Queries).filter(Queries.username == user)
            dbsession.close()
            return render_template("detailsindb.html", DATA = results)
        else:
            dbsession.close()
            return render_template("customer.html")   
    else:
        help = request.form.get("help")
        user = session["user_id"]
        dbsession = Session()
        obj4 = Queries(user,help)
        dbsession.add(obj4)
        dbsession.commit()
        dbsession.close()
        return render_template("thankyou.html")


@app.route("/forgotpassword", methods=["POST","GET"])
def forgotpassword():
    if request.method == "GET":
        return render_template("forgotpassword.html")

    else:
        user = request.form.get("username")
        question = request.form.get("recoverpass")
        answer = request.form.get("ans")

        dbsession = Session()
        exists = dbsession.query(Recover).filter( Recover.username == user).filter(Recover.question == question).filter(Recover.answer == answer).scalar()
        if exists is not None:
            results = dbsession.query(User).filter(User.username == user)
            resultemail = dbsession.query(Details).filter(Details.username == user)

            body = 'Your Password: ' + results[0].hash
            sendEmail( resultemail[0].email, "password recovery",  body)
            dbsession.close() 
            return render_template("common.html", value = "Please check your Email for Password recovery!")
        else:
            dbsession.close()
            return render_template("common.html", value = "Your data does not exist, please enter correct information")
    