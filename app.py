import os
from flask import (
    Flask, render_template, request, flash, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

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


# logout current user
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# show scholarships listed in database
@app.route("/get_scholarships")
def get_scholarships():
    scholarships = mongo.db.scholarships.find(
        {"scholarship_status": "Active"}
    )
    return render_template("scholarships.html",
                           scholarships=scholarships)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    scholarships = list(mongo.db.scholarships.find(
        {"scholarship_status": "Active",
         "$text": {"$search": query}
         }))
    return render_template("scholarships.html",
                           scholarships=scholarships)


# view selected scholarship details
@app.route("/view_scholarship/<scholarship_id>", methods=["GET"])
def view_scholarship(scholarship_id):
    scholarship = mongo.db.scholarships.find_one(
        {"_id": ObjectId(scholarship_id)})
    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
    return render_template("view_scholarship.html",
                           scholarship=scholarship,
                           categories=categories,
                           statuses=statuses)


# add new scholarship
@app.route("/add_scholarship", methods=["GET", "POST"])
def add_scholarship():
    if request.method == "POST":
        scholarship = {
            "scholarship_name": request.form.get("scholarship_name"),
            "scholarship_sponsor": request.form.get("scholarship_sponsor"),
            "category": request.form.get("category"),
            "scholarship_amount": request.form.get("scholarship_amount"),
            "scholarship_url": request.form.get("scholarship_url"),
            "scholarship_deadline": request.form.get("scholarship_deadline"),
            "date_winner_announced": request.form.get("date_winner_announced"),
            "note": request.form.get("note"),
            "dates": {
                "date_applied": "2000-01-01",
                "date_awarded": "2000-01-01",
                "date_rejected": "2000-01-01",
                "date_declined": "2000-01-01"
            },
            "application_status": "Information",
            "scholarship_status": "Active",
            "created_by": "alivia@example.com",
            # "created_by": session["user"],
            "create_date": datetime.datetime.now()
        }
        mongo.db.scholarships.insert_one(scholarship)
        flash("Scholarship Successfully Added")
        return redirect(url_for("get_scholarships"))

    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
    return render_template("add_scholarship.html",
                           categories=categories,
                           statuses=statuses)


# edit existing scholarship
@app.route("/edit_scholarship/<scholarship_id>", methods=["GET", "POST"])
def edit_scholarship(scholarship_id):
    if request.method == "POST":
        scholarship = {
            "scholarship_name": request.form.get("scholarship_name"),
            "scholarship_sponsor": request.form.get("scholarship_sponsor"),
            "category": request.form.get("category"),
            "scholarship_amount": request.form.get("scholarship_amount"),
            "scholarship_url": request.form.get("scholarship_url"),
            "scholarship_deadline": request.form.get("scholarship_deadline"),
            "date_winner_announced": request.form.get("date_winner_announced"),
            "note": request.form.get("note"),
            "dates": {
                "date_applied": request.form.get("date_applied"),
                "date_awarded": request.form.get("date_awarded"),
                "date_rejected": request.form.get("date_rejected"),
                "date_declined": request.form.get("date_declined")
            },
            "application_status": request.form.get("application_status"),
            "scholarship_status": "Active",
            "created_by": "alivia@example.com",
            # "created_by": session["user"],
            "updated_by": "alivia@example.com",
            # "updated_by": session["user"],
            "last_updated": datetime.datetime.now()
        }
        mongo.db.scholarships.update(
            {"_id": ObjectId(scholarship_id)}, scholarship)
        flash("Scholarship Successfully Updated")

    scholarship = mongo.db.scholarships.find_one(
        {"_id": ObjectId(scholarship_id)})
    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
    return render_template("edit_scholarship.html",
                           scholarship=scholarship,
                           categories=categories,
                           statuses=statuses)


# delete existing scholarship
@app.route("/delete_scholarship/<scholarship_id>", methods=["GET"])
def delete_scholarship(scholarship_id):
    scholarship = mongo.db.scholarships.find_one(
        {"_id": ObjectId(scholarship_id)})
    mongo.db.scholarships.remove({"_id": ObjectId(scholarship_id)})
    flash("Scholarship Successfully Deleted")
    return render_template("scholarships.html",
                           scholarship=scholarship)


# view admin panel to manage items in database
@app.route("/get_adminpanel", methods=["GET"])
def get_adminpanel():
    return render_template("admin.html")


# view existing categories via admin panel
@app.route("/get_categories", methods=["GET", "POST"])
def get_categories():
    categories = list(mongo.db.categories.find().sort("category", 1))
    return render_template("categories.html", categories=categories)


# add new category via admin panel
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Successfully Added")
        return redirect(url_for("get_categories"))
    categories = list(mongo.db.categories.find().sort("category", 1))
    return render_template("add_category.html", categories=categories)


# edit existing category via admin panel
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, category)
        flash("Category Successfully Updated")
    return redirect(url_for("get_categories",
                            category=category))


# delete existing category via admin panel
@app.route("/delete_category/<category_id>", methods=["GET", "POST"])
def delete_category(category_id):
    category = mongo.db.categories.find({"_id": ObjectId(category_id)})
    if request.method == "POST":
        category = mongo.db.categories.find({"_id": ObjectId(category_id)})
        mongo.db.categories.remove({"_id": ObjectId(category_id)}, category)
        flash("category Successfully Deleted")
        return redirect(url_for("get_categories",
                                category=category))
    flash("Are you sure you want to delete this category?")
    categories = list(mongo.db.categories.find().sort("category", 1))
    return render_template("delete_category.html",
                           categories=categories)


# view existing statuses via admin panel
@app.route("/get_statuses", methods=["GET", "POST"])
def get_statuses():
    statuses = list(mongo.db.statuses.find().sort("status", 1))
    return render_template("statuses.html", statuses=statuses)


# add new status via admin panel
@app.route("/add_status", methods=["GET", "POST"])
def add_status():
    if request.method == "POST":
        status = {
            "status": request.form.get("status")
        }
        mongo.db.statuses.insert_one(status)
        flash("Status Successfully Added")
        return redirect(url_for("get_statuses"))
    statuses = list(mongo.db.statuses.find().sort("status", 1))
    return render_template("add_status.html", statuses=statuses)


# edit existing status via admin panel
@app.route("/edit_status/<status_id>", methods=["GET", "POST"])
def edit_status(status_id):
    if request.method == "POST":
        status = {
            "status": request.form.get("status")
        }
        mongo.db.statuses.update(
            {"_id": ObjectId(status_id)}, status)
        flash("Status Successfully Updated")
    return redirect(url_for("get_statuses",
                            status=status))


# delete existing status via admin panel
@app.route("/delete_status/<status_id>", methods=["GET", "POST"])
def delete_status(status_id):
    status = mongo.db.statuses.find({"_id": ObjectId(status_id)})
    if request.method == "POST":
        status = mongo.db.statuses.find({"_id": ObjectId(status_id)})
        mongo.db.statuses.remove({"_id": ObjectId(status_id)}, status)
        flash("Status Successfully Deleted")
        return redirect(url_for("get_statuses",
                                status=status))
    flash("Are you sure you want to delete this status?")
    statuses = list(mongo.db.statuses.find().sort("status", 1))
    return render_template("delete_status.html",
                           statuses=statuses)


# view existing users via admin panel
@app.route("/get_users", methods=["GET", "POST"])
def get_users():
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("users.html", users=users)


# add new user via admin panel
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        user = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "create_date": datetime.datetime.now()
        }
        mongo.db.users.insert_one(user)
        flash("user Successfully Added")
        return redirect(url_for("get_users"))
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("add_user.html", users=users)


# edit existing user via admin panel
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.method == "POST":
        user = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "create_date": datetime.datetime.now()
        }
        mongo.db.users.update(
            {"_id": ObjectId(user_id)}, user)
        flash("User Successfully Updated")
    return redirect(url_for("get_users",
                            user=user))


# delete existing user via admin panel
@app.route("/delete_user/<user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    user = mongo.db.users.find({"_id": ObjectId(user_id)})
    if request.method == "POST":
        user = mongo.db.users.find({"_id": ObjectId(user_id)})
        mongo.db.users.remove({"_id": ObjectId(user_id)}, user)
        flash("User Successfully Deleted")
        return redirect(url_for("get_users",
                                user=user))
    flash("Are you sure you want to delete this user?")
    users = list(mongo.db.users.find().sort("user", 1))
    return render_template("delete_user.html",
                           user=user,
                           users=users)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
