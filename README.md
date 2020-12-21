<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Scholarship Tracker

Purpose: To allow user to create and update a list of scholarships.

Project is deployed to https://scholarshiptracker.herokuapp.com/.

Scholarship data to include Name, Sponsor, website, amount, deadline, documents required (including count of recommendations and essays), date applied, and date winner to be announced.

User will be able to complete profile information to be used in the future.

User will be able to view page about website creation and contact site owner with form.

## UI/UX

Home page
- shows register user form
- shows sign in form
- shows link to contact form
- shows link to about page
- shows footer with copyright

User page
- shows list of stored scholarships
- displays button linking to add scholarship form
- displays button linking to edit scholarship form
- displays button linking to remove scholarship from displayed list
- allows search of scholarship by Name
- allows filter by category

Scholarship displays:
- Name
- Sponsor
- amount
- deadline
- documents required:
* recommendations
* recommendation count
* transcript
* essays
* essay count
* 3 other document items
- notes
- status
* plan to apply
* applied
* awarded
* not awarded
* declined
- date applied
- date winner announced
- website

Admin page
- manage users

Nice to haves
- user profile
- user dashboard
* total scholarship count
* applied for vs total count
* accepted scholarship vs applied for
* deadline within 30, 60, or 90 displays
- deadline in red when past due
- awarded in red when past due
- link to url
- email notification of deadlines