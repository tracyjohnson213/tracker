import os
from flask import (
    Flask, render_template, request, flash, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user into session cookie
        session["user"] = request.form.get("email").lower()
        session["first_name"] = request.form.get("first_name").capitalize()
        flash("Registration sucessful!")
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/get_scholarships")
def get_scholarships():
    scholarships = mongo.db.scholarships.find()
    return render_template("scholarships.html",
                           scholarships=scholarships)


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
