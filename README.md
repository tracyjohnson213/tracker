<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

# Scholarship Tracker

Purpose: To allow user to create and update a list of scholarships.

Project is deployed to https://scholarshiptracker.herokuapp.com/.

Scholarship data to include Name, Sponsor, website, amount, deadline, documents required (including count of recommendations and essays), date applied, and date winner to be announced.

User will be able to complete profile information to be used in the future.

User will be able to view page about website creation and contact site owner with form.

## UI/UX

User Stories:
    * As a user, I want to register my email, in order to gain a login to access the application.
    * As a system, I want to store the user password encrypted, in order to provide security of user data.
    * :thumbsdown: As a user, I want to log into the application, in order to add scholarships for tracking.
    * As a user, I want to view all scholarships previously added for tracking, in order to compare deadlines.
    * :thumbsdown: As a system, I want to display only the scholarships that have been stored by a specific user, in order to not provide incorrect data.
    * As a user, I want to view all scholarships previously added for tracking, in order to compare status.
    * As a user, I want to edit a scholarship, in order to update the related information.
    * As a user, I want to remove a scholarships, in order to longer view it as a tracked scholarship. 
    * As a user, I want to link to the url of a scholarship or sponsor, in order to gain information not recorded in the application.

Nice to haves
    * As a user, I want to view information about the application or site owner, in order to build a rapport with the site owner.
    * As a user, I want to contact the site owner within the application, in order to share information.
- user dashboard
    * total scholarship count
    * applied for vs total count
    * accepted scholarship vs applied for
    * deadline within 30, 60, or 90 displays
- deadline in red when past due
- awarded in red when past due
- scholarship status to record if plan to apply, applied, awarded, or award denied
- scholarship documents required
- email notification of deadlines

## Features

View Scholarships:
Scholarships with deadline in past show with red colored tag.
Scholarships with deadline within 30 days show with yellow colored tag.
Add/Edit Scholarships:
Associated documents for scholarship can be listed with quantity.
Custom named documents for scholarship can be save as Required or Optional.
Input field displayed when Other selected as Category and Status during Add Scholarship and Edit Scholarship.
Category and Status list updated with submit of input to Other field.
Category and Status can be removed from Add and Edit forms.


## Technologies Used

https://www.html5pattern.com/Passwords
https://materializecss.com/

## Testing

1. Home page
    * Verify display of marketing text
    * Verify display of Register form
    * Verify display of Login button
1. Registration page
    * Try to submit registration without first name and verify display of error message about required field.
    * Try to submit registration without last name and verify display of error message about required field.
    * Try to submit registration without email and verify display of error message about required field.
    * Try to submit registration without password and verify display of error message about required field.
    * Try to submit registration with no data and verify display of error message about required fields.
    * Try to submit registration with invalid email and verify display of error message about valid format.
    * Try to submit registration with invalid password and verify display of error message about valid format.
    * Try to submit registration with valid set of data and verify display message about sucessful registration.
1. Login page
    * Try to login with email that does not exist in database and verify display of error message.
    * Try to login without email and verify display of error message about required field.
    * Try to login without password and verify display of error message about required field.
1. User - Logout page
    * Verify display of logout confirmation
1. Scholarship List page
    * Verify scholarship name is displayed
    * Verify scholarship sponsor is displayed
    * Verify scholarship award amount is displayed
    * Verify scholarship deadline is displayed
    * Verify scholarship website address is displayed
    * Verify scholarship website links to new page with results of listed url
    * Verify scholarship name links to page with more details
1. Scholarship Details page
    * Verify scholarship name is displayed
    * Verify scholarship sponsor is displayed
    * Verify scholarship award amount is displayed
    * Verify scholarship deadline is displayed
    * Verify scholarship website address is displayed
    * Verify date to announce winner of scholarship is displayed
    * Verify inputted notes for scholarship are displayed
    * Verify scholarship website links to new page with results of listed url
    * Verify edit button is displayed
    * Verify edit button links to new page displaying input fields with data
    * Verify delete button is displayed
1. Add Scholarship page
    * Try to add scholarship without name and verify error is displayed
    * Try to add scholarship with only name
1. edit
1. delete
    * Try to delete scholarship and cancel confirmation of deletion to verify scholarship remains in list of all scholarships
    * Try to delete scholarship and confirm deletion to verify scholarship no longer displays in list of all scholarships

1. Look and Feel in browsers
1. Bugs
    * (Login Page) Try to login with valid email and password combination and verify display of /scholarships.
    * (Scholarship Details page) Verify delete button leads to new page requesting confirmation before deleting
    * Verify Login button is not displayed after login
    * Verify Logout button is not displayed before login
    * Verify navigation link to view all is not displayed after logout
    * Verify all scholarships are displayed after delete of one

## Deployment

## Credits

Favicon - https://www.freefavicon.com/freefavicons/business/iconinfo/graduation-cap-152-190967.html
Login form for materialize - https://codepen.io/T-P/pen/bpWqrr
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
https://stackoverflow.com/questions/29321494/show-input-field-only-if-a-specific-option-is-selected

## Media

- content used 
Scholarship list - https://docs.google.com/document/d/1hpL9JWL9nTBt9VoTfrIMW1Ie5sO5LvZmkWs8oDuHlBk/edit

## Acknowledgements

