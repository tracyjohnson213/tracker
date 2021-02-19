
<img  src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png"  style="margin: 0;" alt="Code Institute">

# Scholarship Tracker

Purpose: To allow user to create and update a list of scholarships.

Project is deployed to https://scholarshiptracker.herokuapp.com/.

Scholarship data to include Name, Sponsor, website, amount, deadline, documents required (including count of recommendations and essays), date applied, and date winner to be announced.

User will be able to complete profile information to be used in the future.

User will be able to view page about website creation and contact site owner with form.

## UI/UX

Wireframes created with Figma: [Wireframe](../static/docs/tracker.pdf)

User Stories:

* As a user, I want to register my email, in order to gain a login to access the application.

* As a system, I want to store the user password encrypted, in order to provide security of user data.

* As a user, I want to log into the application, in order to add scholarships for tracking.

* As a user, I want to view all scholarships previously added for tracking, in order to compare deadlines and other details.

* As a system, I want to display only the scholarships that have been stored by a specific user, in order to not provide incorrect data.

* As a user, I want to add scholarships for tracking, in order to compare details.

* As a user, I want to edit a scholarship, in order to update the related details.

* As a user, I want to remove a scholarships, in order to longer view it as a tracked scholarship.

* As a user, I want to link to the url of a scholarship or sponsor, in order to gain information not recorded in the application.

* As a user, I want to filter scholarships by set category.

* As a user, I want to filter scholarships by set status.

* As a user, I want to search scholarships by name.

* As a user, I want to easily distinguish when deadlines are past.

* As a user, I want to easily distinguish when deadlines are near.

* As a user, I want to see a list of documents required for a scholarship.

* As a user, I want to see a list of dates associated to a scholarship.


## Features

1. Register new user.

1. Authenticate and login existing user.

1. Add scholarship with details.

1. View scholarship with details.

1. Edit scholarship details.

1. Delete scholarship.

1. Search scholarship by name.

1. Filter scholarship list by category.

1. Filter scholarship list by status.

1. Logout

1. Scholarships with deadline in past show with red colored tag.

1. Scholarships with deadline within 30 days show with yellow colored tag.

1. Associate quantity with document for scholarship.

1. Associate custom named document with scholarship as Required or Optional.

1. Admin panel to add, edit, and remove users

### Features left to implement

* As a user, I want to view information about the application or site owner, in order to build a rapport with the site owner.

* As a user, I want to contact the site owner within the application, in order to share information.

* As a user, I want to view a user dashboard with a total scholarship count

* As a user, I want to view a user dashboard to view applied for vs total scholarship count

* As a user, I want to view a user dashboard to view accepted vs applied for scholarships

* As a user, I want to receive email notification of deadlines

* As a user, I want to limit the number of scholarships I view

* As a user, I want to use pagination to see sets of scholarships

* As a user, I want to delete my account

* As a user, I want to recover my password

* As an admin, I want to use a panel to add, edit, and remove categories

* As an admin, I want to use a panel to add, edit, and remove statuses

* As an admin, I want to reset a user's password

## Technologies Used


HTML5 - The project uses HTML5, a markup language used for structuring and presenting content on the World Wide Web.

CSS3 - The project uses Cascading Style Sheets(CSS), a style sheet language used for describing the presentation of a document written in a markup language like HTML.

JavaScript - The project uses JavaScript, a programming language that conforms to the ECMAScript specification.

Python - The project uses Python, an interpreted, high-level, general-purpose programming language.

Flask - The project uses Flask, which depends on the Jinja template engine and the Werkzeug WSGI toolkit.

MongoDB - The project uses MongoDB, is a popular database for modern apps, and MongoDB Atlas, the global cloud database on AWS, Azure, and GCP. My database consist of collections for scholarships, categories, statues, and users.

Gitpod - Gitpod is a development environment for any GitLab, GitHub, and Bitbucket project.

Github - Github is a repository hosting service.

Heroku - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

StackEdit - README.md was generated within StackEdit, a full-featured, open-source Markdown editor based on PageDown, the Markdown library used by Stack Overflow and the other Stack Exchange sites.

Unittest - unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

Figma - free, online UI tool for design and prototypes.

# Database collections

scholarships = {
    "_id": "",
    "scholarship_name": "Create-A-Greeting-Card Scholarship",
    "scholarship_sponsor": "The Gallery Collection",
    "category": "College",
    "scholarship_amount": "10,000",
    "scholarship_url":
        "https://www.gallerycollection.com/greeting-cards-scholarship.htm",
    "scholarship_deadline": "2021-03-09",
    "date_winner_announced": "2021-05-17",
    "note": "Submit original photo, artwork or computer graphics for the front of a greeting card.",
    "dates": {
        "date_applied": "2000-01-01",
        "date_awarded": "2000-01-01",
        "date_rejected": "2000-01-01",
        "date_declined": "2000-01-01"
        },
    "application_status": "Information",
    "scholarship_status": "Active",
    "created_by": "alivia@example.com",
    "create_date": datetime.now()
}

categories = {
    "_id": "",
    "category": "Information to Know"
}

statuses = {
    "_id": "",
    "status": "Plan to Apply"
}

users = {
    "_id": "",
    "first_name": "",
    "last_name": "",
    "username": "",
    "password": "",
    "role": "",
    "create_date": "",
    "last_login": ""
}

# Libraries:

jQuery - JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax.

Materialize CSS - modern responsive CSS framework based on Material Design by Google

# Resources:

https://www.html5pattern.com/Passwords

# Validation

- https://validator.w3.org/ to validate the HTML code.

- https://jigsaw.w3.org/css-validator/ to validate the CSS code.

- https://jshint.com/ to check the JavaScript code.

- gitpod used to check Python code for PEP.

## Testing

Home page

- [ ] Verify display of marketing text.

- [ ] Verify display of Register form.

- [ ] Verify display of Login button.

- [ ] Verify display of logo.

Registration form

- [ ] Try to submit registration without first name and verify display of error message about required field.

- [ ] Try to submit registration without last name and verify display of error message about required field.

- [ ] Try to submit registration without email and verify display of error message about required field.

- [ ] Try to submit registration without password and verify display of error message about required field.

- [ ] Try to submit registration with no data and verify display of error message about required fields.

- [ ] Try to submit registration with invalid email and verify display of error message about valid format.

- [ ] Try to submit registration with invalid password and verify display of error message about valid format.

- [ ] Try to submit registration with valid set of data and verify display message about sucessful registration and login page.

Login page

- [ ] Try to login with email that does not exist in database and verify display of error message.

- [ ] Try to login without email and verify display of error message about required field.

- [ ] Try to login without password and verify display of error message about required field.

- [ ] Try to login with valid credientials to view empty scholarship list.

Scholarship List page

- [ ] Verify welcome message to user displayed with first name

- [ ] Verify scholarship name is displayed.

- [ ] Verify scholarship sponsor is displayed.

- [ ] Verify scholarship award amount is displayed.

- [ ] Verify scholarship deadline is displayed.

- [ ] Verify scholarship website address is displayed.

- [ ] Verify scholarship website links to new page with results of listed url.

- [ ] Verify click scholarship name expands pane with scholarship details.

- [ ] Verify deadlines that are past due display in red.

- [ ] Verify deadlines within 30 display in yellow.

Scholarship Details pane

- [ ] Verify scholarship name is displayed.

- [ ] Verify scholarship sponsor is displayed.

- [ ] Verify scholarship award amount is displayed.

- [ ] Verify scholarship deadline is displayed.
 
- [ ] Verify scholarship website address is displayed.

- [ ] Verify date to announce winner of scholarship is displayed.

- [ ] Verify inputted notes for scholarship are displayed.

- [ ] Verify scholarship website links to new page with results of listed url.

- [ ] Verify edit button is displayed.

- [ ] Verify edit button links to new page displaying input fields with data.

- [ ] Verify delete button is displayed.

- [ ] Verify display of Add Scholarship button.

Filter by category

- [ ] Verify update of results when category is selected.

- [ ] Verify update of results when reset is clicked.

Filter by status

- [ ] Verify update of results when category is selected.

- [ ] Verify update of results when reset is clicked.

Search by scholarship name

- [ ] Try to click search without input of name to verify display of message.

- [ ] Verify update of results when name is inputted before search is clicked.

- [ ] Verify update of results when reset is clicked.

- [ ] Verify no records found when name is inputted that is not in list of scholarships.

Add Scholarship form

- [ ] Try to add scholarship without name and verify error is displayed.

- [ ] Try to add scholarship with only name.


- [ ] Try to add scholarship(s) with various field values and verify update to details.

Edit Scholarship form

- [ ] Update each field and click update to verify value updated in details.

Delete Scholarship


- [ ] Try to delete scholarship and cancel confirmation of deletion to verify scholarship remains in list of all scholarships

- [ ] Try to delete scholarship and confirm deletion to verify scholarship no longer displays in list of all scholarships

Logo

- [ ] Verify display of logo and link back to view of all scholarships.

User - Logout page

- [ ] Verify display of logout confirmation

Error handling

- [ ] Edit a scholarship and try to update the url by removing one or more characters and refresh the page to verify 500 error page.

- [ ] View all scholarships and try to update the url by removing one or more characters and refresh the page to verify the 4040 error page.

Admin Panel

- [ ] Try to add user without email to verify error displayed

- [ ] Try to add user without first name to verify error displayed

- [ ] Try to add user without last name to verify error displayed

- [ ] Try to add user with all inputs and Admin role to verify user added to full list with Admin role

- [ ] Try to add user with all inputs and Student role to verify user added to full list with Student role

- [ ] Verify logged in user is not able to delete self

- [ ] Verify no user is not able to delete Primary Admin user (harry.potter@example.com, 1Student!)

Responsive Design

- [ ] Test for responsive design in desktop, tablet, and mobile views.

Unittests

The tests are saved in the folder tests. In order to run the tests I typed the following on the terminal:
 
```
python3 -m unittest -v tests/*
```

Results:
Ran 23 tests in 1.933s
FAILED (errors=6)

## Bugs


* (Scholarship List page) Dates should display in m-d-Y format.

* (Scholarship List page) Filter Categories, All Categories should reset list displayed.

* (Scholarship List page) Filter Statuses should reset list displayed.

* (Add Scholarship) Date applied should be limited to after deadline.

* (Add Scholarship) Date awarded should be limited to after winner announced.

* (Add Scholarship) When document with quantity field selected value should update to 1.

* (Add Scholarship) Input of note should start at left.

* (Edit Scholarship) Display award amount from scholarship details.

* (Edit Scholarship) Display note from scholarship details.

* (Edit Scholarship) When document with quantity field selected value should update to 1.

* (Filter by status) Results should update when status is selected from dropdown.

* (Admin - Add user) System should assign default password to user and notify them by email.

## Deployment


1. I created a Github repository and opened the repository in Gitpod IDE.

1. I installed Flask, Flask-pymongo and dnspython.

1. I created an env.py file that contains my environment variables.

    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY", "")
    os.environ.setdefault("MONGO_URI", "")
    os.environ.setdefault("MONGO_DBNAME", "tracker")
    os.environ.setdefault("TEST_MONGODB_URI", "")
    ```

1. I created a new app in Heroku.

1. I created requirements.txt and Procfile that Heroku requires to run the app.

1. I pushed both files to GitHub.

1. On the Deploy tab in Heroku I enabled automatic deploys to the master branch.

## Credits

 
[Favicon](https://www.freefavicon.com/freefavicons/business/iconinfo/graduation-cap-152-190967.html)

[Login form for materialize](https://codepen.io/T-P/pen/bpWqrr)

[Flask Authentication](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)


[Flask Unittest Tutorial](http:www.patricksoftwareblog.com/unit-testing-a-flask-application/)


## Media


- content used
[Scholarship list](https://docs.google.com/document/d/1hpL9JWL9nTBt9VoTfrIMW1Ie5sO5LvZmkWs8oDuHlBk/edit)

## Acknowledgements


Thanks to my Mentor Guido Cecilio Garcia Bernal for offering guidance, constructive crticism, and patience on my long process. I have gained confidence from my projects with CodeInstite and hope to grow with the experience.

Thank you also to my daughter who is a high school senior. She inspired this project by looking for a better way to track her college scholarships. She currently has improved a collection on Google Sheets and has shared it with her high school class.


## Disclaimer


The page has been created for educational purpose only, not for commercial use.