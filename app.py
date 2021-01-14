import os
from flask import (
    Flask, render_template, request, flash, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


# register new user
@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This email already exists.")
            flash("Please login or try a different email.")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(
                    request.form.get("password")),
            "create_date": datetime.datetime.now()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("first_name").title()
        flash("Registration Successful!")

    return render_template("register.html")


# login as existing user
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("first_name").title()
                flash("Welcome, {}".format(request.form.get("first_name")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# show scholarships listed in database
@app.route("/get_scholarships")
def get_scholarships():
    scholarships = mongo.db.scholarships.find()
    return render_template("scholarships.html",
                           scholarships=scholarships)


# view selected scholarship details
@app.route("/view_scholarship/<scholarship_id>", methods=["GET"])
def view_scholarship(scholarship_id):
    scholarship = mongo.db.scholarships.find_one(
        {"_id": ObjectId(scholarship_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("view_scholarship.html",
                           scholarship=scholarship,
                           categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
