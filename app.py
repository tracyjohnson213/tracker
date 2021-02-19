import os
from flask import (
    Flask, render_template, request, flash, redirect, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import HTTPException
from datetime import datetime, timedelta

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
            "create_date": datetime.now()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        session["role"] = "Student"
        flash("Registration Successful!")
        return redirect(url_for("login"))

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
                session["user"] = request.form.get("username").lower()
                session["role"] = existing_user["role"]
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("get_scholarships",
                                username=session["user"],
                                role=session["role"]))
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
    flash("You have been logged out.  Thanks.  Please visit us again.")
    session.pop("user")
    return redirect(url_for("login"))


# show scholarships listed in database
@app.route("/get_scholarships", methods=["GET"])
def get_scholarships():
    if session["user"]:
        user = mongo.db.users.find_one_or_404({"username": session["user"]})
        categories = list(mongo.db.categories.find())
        statuses = list(mongo.db.statuses.find())
        users = list(mongo.db.users.find())
        scholarships = mongo.db.scholarships.find(
            {"created_by": user['username']}
        ).sort("scholarship_deadline", 1)
        today = datetime.now()
        endate = datetime.now() + timedelta(30)
        return render_template("scholarships.html",
                               scholarships=scholarships,
                               categories=categories,
                               statuses=statuses,
                               users=users,
                               today=today,
                               endate=endate)
    return redirect(url_for("login"))


# show scholarships with specific category
@app.route("/get_scholarships/<category>", methods=["GET"])
def get_category(category):
    if session["user"]:
        user = mongo.db.users.find_one_or_404(
            {"username": session["user"]})
        categories = list(mongo.db.categories.find(
            {"category": category}
        ))
        statuses = list(mongo.db.statuses.find())
        users = list(mongo.db.users.find())
        scholarships = mongo.db.scholarships.find(
            {"created_by": user['username'],
             "category": category}
        ).sort("scholarship_deadline", 1)
        today = datetime.now()
        endate = datetime.now() + timedelta(30)
        return render_template("scholarships.html",
                               scholarships=scholarships,
                               categories=categories,
                               statuses=statuses,
                               users=users,
                               today=today,
                               endate=endate)


# show scholarships with specific status
@app.route("/get_scholarships/<status>", methods=["GET"])
def get_status(status):
    if session["user"]:
        user = mongo.db.users.find_one_or_404(
            {"username": session["user"]})
        categories = list(mongo.db.categories.find())
        statuses = list(mongo.db.statuses.find(
            {"status": status}
        ))
        users = list(mongo.db.users.find())
        scholarships = mongo.db.scholarships.find(
            {"created_by": user['username'],
             "status": status}
        ).sort("scholarship_deadline", 1)
        today = datetime.now()
        endate = datetime.now() + timedelta(30)
        return render_template("scholarships.html",
                               scholarships=scholarships,
                               categories=categories,
                               statuses=statuses,
                               users=users,
                               today=today,
                               endate=endate)


# search scholarship by text
@app.route("/search", methods=["GET", "POST"])
def search():
    if session["user"]:
        user = mongo.db.users.find_one_or_404({"username": session["user"]})
        query = request.form.get("query")
        scholarships = list(mongo.db.scholarships.find(
            {"created_by": user['username'],
             "scholarship_status": "Active",
             "$text": {"$search": query}
             }))
        today = datetime.now()
        endate = datetime.now() + timedelta(30)
        return render_template("scholarships.html",
                               scholarships=scholarships,
                               today=today,
                               endate=endate)


# view selected scholarship details
@app.route("/view_scholarship/<scholarship_id>", methods=["GET"])
def view_scholarship(scholarship_id):
    scholarship = mongo.db.scholarships.find_one_or_404(
        {"_id": ObjectId(scholarship_id)})
    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
    today = datetime.now()
    endate = datetime.now() + timedelta(30)
    return render_template("view_scholarship.html",
                           scholarship=scholarship,
                           categories=categories,
                           statuses=statuses,
                           today=today,
                           endate=endate)


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
                "date_applied": request.form.get("date_applied"),
                "date_awarded": request.form.get("date_awarded"),
                "date_rejected": request.form.get("date_rejected"),
                "date_declined": request.form.get("date_declined"),
            },
            "documents": {
                "recommendation_required":
                request.form.get("recommendation_required"),
                "recomendation_count": request.form.get("recomendation_count"),
                "transcript_required": request.form.get("transcript_required"),
                "transcript_count": request.form.get("transcript_count"),
                "essay_required": request.form.get("essay_required"),
                "essay_count": request.form.get("essay_count"),
                "other1": {
                    "document_name": request.form.get("document_name1"),
                    "required": request.form.get("document_required1")
                },
                "other2": {
                    "document_name": request.form.get("document_name2"),
                    "required": request.form.get("document_required2")
                },
                "other3": {
                    "document_name": request.form.get("document_name3"),
                    "required": request.form.get("document_required3")
                }
            },
            "application_status": "Information",
            "scholarship_status": "Active",
            "created_by": session["user"],
            "create_date": datetime.now()
        }
        mongo.db.scholarships.insert_one(scholarship)
        flash("Scholarship Successfully Added")
        return redirect(url_for("get_scholarships",
                                username=session["user"]))

    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
    return render_template("add_scholarship.html",
                           categories=categories,
                           statuses=statuses)


# edit existing scholarship
@app.route("/edit_scholarship/<scholarship_id>", methods=["GET", "POST"])
def edit_scholarship(scholarship_id):
    categories = mongo.db.categories.find().sort("category", 1)
    statuses = mongo.db.statuses.find().sort("status", 1)
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
            "documents": {
                "recommendation_required":
                request.form.get("recommendation_required"),
                "recomendation_count": request.form.get("recomendation_count"),
                "transcript_required": request.form.get("transcript_required"),
                "transcript_count": request.form.get("transcript_count"),
                "essay_required": request.form.get("essay_required"),
                "essay_count": request.form.get("essay_count"),
                "other1": {
                    "document_name": request.form.get("document_name1"),
                    "required": request.form.get("document_required1")
                },
                "other2": {
                    "document_name": request.form.get("document_name2"),
                    "required": request.form.get("document_required2")
                },
                "other3": {
                    "document_name": request.form.get("document_name3"),
                    "required": request.form.get("document_required3")
                }
            },
            "application_status": request.form.get("application_status"),
            "scholarship_status": "Active",
            "created_by": session["user"],
            "updated_by": session["user"],
            "last_updated": datetime.now()
        }
        mongo.db.scholarships.update(
            {"_id": ObjectId(scholarship_id)}, scholarship)
        flash("Scholarship Successfully Updated")
        return redirect(url_for("get_scholarships",
                                username=session["user"]))
    scholarship = mongo.db.scholarships.find_one_or_404(
        {"_id": ObjectId(scholarship_id)})

    return render_template("edit_scholarship.html",
                           scholarship=scholarship,
                           categories=categories,
                           statuses=statuses)


# delete existing scholarship
@app.route("/delete_scholarship/<scholarship_id>", methods=["GET"])
def delete_scholarship(scholarship_id):
    mongo.db.scholarships.delete_one({"_id": ObjectId(scholarship_id)})
    flash("Scholarship Successfully Deleted")
    return redirect(url_for("get_scholarships",
                            username=session["user"]))


# view existing users via admin panel
@app.route("/get_users", methods=["GET", "POST"])
def get_users():
    users = list(mongo.db.users.find().sort("username", 1))
    return render_template("users.html", users=users)


# add new user via admin panel
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    # check if username already exists in db
    existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()})
    if existing_user:
        flash("This email already exists.")
        flash("Please login or try a different email.")
        return redirect(url_for("get_users"))

    if request.form.get("role") == "no":
        role = "Student"
    else:
        role = "Admin"

    if request.method == "POST":
        user = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "role": role,
            "create_date": datetime.now()
        }
        mongo.db.users.insert_one(user)
        flash("User Successfully Added")
        return redirect(url_for("get_users"))


# edit existing user via admin panel
@app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if request.form.get("role") == "no":
        role = "Student"
    else:
        role = "Admin"
    if request.method == "POST":
        user = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "role": role,
            "create_date": datetime.now()
        }
        mongo.db.users.update(
            {"_id": ObjectId(user_id)}, user)
        flash("User Successfully Updated")
    return redirect(url_for("get_users"))


# delete existing user via admin panel
@app.route("/delete_user/<user_id>", methods=["GET", "POST"])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("User Successfully Deleted")
    return redirect(url_for("get_users"))


# error handling
@app.errorhandler(HTTPException)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
