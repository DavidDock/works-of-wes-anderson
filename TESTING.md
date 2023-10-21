# CONTENTS

* [User Story Testing](#user-story-testing)
* [Browser Support](#browser-testing)
* [Device Responsiveness](#device-responsiveness)
* [Python Validator](#python-validator)
* [JavaScript Validator](#javascript-validator)
* [HTML Validator](#html-validator)
* [CSS Validator](#css-validator)
* [Lighthouse](#lighthouse)
* [Wave](#wave)
* [Manual Testing](#manual-testing)
* [Other Bugs And Errors](#other-bugs-and-errors)

## User Story Testing  

### 15 Site Admin

#### Acceptance Criteria

The admin page is visible when Admin is logged in

#### Results  

Admin page visible - pass

### 16 Home Page

#### Acceptance Criteria

The about message is displayed on the Home/Landing page

#### Results  

About message visable and also differs for exisiting user - pass

### 17 Initial Navigation Bar

#### Acceptance Criteria

* The navigation bar is visible with all possible links
* The Logo and Home link to Home
* The Home link is active when on this page
* The Footer is at the bottom

#### Results  

* The navigation is visible with all links relevant to member loggin or not - pass
* The logo and home is linked to home page - pass
* The home link is active - pass
* the footer is present - pass

### 18 Add Film Information

#### Acceptance Criteria

The ability for site Admin to create new Film objects on Admin site

#### Results

The admin can add a new film - pass

### 19 View Films On About Page

#### Acceptance Criteria

You can see each film poster on the about page

#### Results

Each poster is displayed on about page - pass

### 20 Film Detail Page

#### Acceptance Criteria

* You can link to a URL for each film
* You can see Film details

#### Results

* Each poster link goes to the relevant film detail page - pass
* Each Film shows relevent information - pass

### 21 Critic Comments

#### Acceptance Criteria

You can see all critic comments about each film

#### Results  

All critics comments can be seen on the relevent film detail page - pass

### 22 Member Registration

#### Acceptance Criteria

A user can register an account

#### Results

A user can register an account, added to the database - pass

### 23 Log In and Log Out

#### Acceptance Criteria

A user can log in and log out

#### Results

A user can login and logout -pass

### 24 View Member Comments

#### Acceptance Criteria

All authorised member comments are displayed on each film detail

#### Results

Once a comment is authorised by admin it is visible in the film detail area - pass

### 25 Member Area Page

#### Acceptance Criteria

Be able to view a member area page where only logged in members can visit

#### Results

If you are a member you can log in and go to a member area - pass

### 26 Member Can Add Comment

#### Acceptance Criteria

* Can add a comment for each film in the member area
* Get notified that comment is waiting for approval when added
* You can see waiting for approval comments in member area
* Comment added to database waiting for approval by admin

#### Results

* You can add a comment for any film you like in a form in the membe area - pass
* If the user posts a comment it gets sent for approval and message sent to the user - pass
* Once the comment is sent for aproval it can be seen in the member area wit awaiting approval style added to it -pass
* Admin able to aprove comment - pass

### 27 Member Can Edit Comments

#### Acceptance Criteria

* Can edit all comments
* Get notified that comment is waiting for approval when edited
* Comment in database edited
* You can see waiting for approval comments in member area

#### Results

* If user presses edit, the form ppultes correctly - pass
* When comment is edited the message reads awiting approval - pass
* Admin can see edited comment - pass
* User can see pending approval message and styles in member area - pass

### 28 Member Can Delete Comments

#### Acceptance Criteria

* You can delete all comments
* You get asked if you are sure
* You see message confirming deletion
* Comment is no longer seen
* Comment gone from database

#### Results  

* User presses confim button and comment deleted - pass
* A message is asked when delete button is pressed and confirm modal is opened - pass
* A message is given when delete is confirmed - pass
* The comment cant be seen in the member area, film area or admin and database - pass 

### 29 Member Can Rate File By Category

#### Acceptance Criteria

* You can add score for Comedy, Style and Story for each film
* You can see added score in member area
* Message that score has been added
* Score added to database

#### Results  

* The rating can be added and seen in the member area and added to the database - pass
* A successful messge is sent when a valid score is sent - pass

### 30 Ability For Member To Delete Score

#### Acceptance Criteria

* Can delete score
* User asked for confirmation
* User gets message confirming deletion
* Score deleted from database

#### Results

* The User can delete a score with confimation message from website and databae - pass
* It was decided that no confirmation question was nedded to impove ux

### 31 View Average Scores

#### Acceptance Criteria

Can see average score for Comedy, Style and Story for each film in film_detail.html

#### Results

### 37 Favicon

#### Acceptance Criteria

Favicon visible

#### Results

Favicon visible - pass

### 38 Error Pages

#### Acceptance Criteria

* If an error occurs the relevant custom page is shown
* There is a link to the home page

#### Results  

Error pages created and shown for relevant error with link to home page - pass

## Browser Testing

The website was tested with Google Chrome, Microsoft Edge and Safari.  

There were no issuses with Google Chrome and Microsoft Edge.  

Issues and fixes for Safari:

Please note that I was only able to test the website on an IPad and not on a mac but hopefully most issues were highlighted and fixed.  

* A large design aspect for this website is using horizontal scoll containers for comments.  
   Sadly Safari do not allow custom scroll bars. This website uses unique colors for each film scroll bar but Safari do not recogise these. It does not overly effect the overall design but I made sure that the user knew that they had to scroll cross by adding the word scroll in the member area and making sure an overlap of the next scroll item was seen.  
* The footer icons appeard stretched so a fixed height was needed to fix the issue.
* The default colors for Safari and bootstrap seemed to fight . CSS was added to overide the problems. The main problem was in submit buttons where the text couldn't be seen because the default was white text so it was needed to be change to black to fix the issue.

## Device Responsiveness

Responsiveness was tested throughout the development by using dev tools on every section of the site.  
I focused on whether the site works on small devices of 300px wide and also the larger breakpoint of 1024px plus wide. This website is fully responsive on all devices.  
The use of bootstap responsive classes were used on most of the features to ensure responsivness but the odd media query was added when needed.  
As well as using [responsivedesignchecker.com](https://www.responsivedesignchecker.com
) on avaliable pages the reponsivness was tested on various mobile phone and laptop.  
Lots of adjustments throughtout development were made to ensure responsive design.  

## Python Validator

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to test the python code.  

The validation was done to all the custom python files written for this site. Settings.py was not included because it contains important data which is longer than 79 lines and can not be ajusted.  
No problems found, see results below.

### context_processors.py

<details><summary>Validator</summary>

![Context Processors](documentation/testing/context-processors.png)
</details>

### worksofwes urls.py

<details><summary>Validator</summary>

![worksofwes urls](documentation/testing/worksofwes-urls.png)
</details>

### admin.py

<details><summary>Validator</summary>

![Admin](documentation/testing/admin.png)
</details>

### apps.py

<details><summary>Validator</summary>

![Apps](documentation/testing/apps.png)
</details>

### forms.py

<details><summary>Validator</summary>

![Forms](documentation/testing/forms.png)
</details>

### models.py

<details><summary>Validator</summary>

![Models](documentation/testing/models.png)
</details>

### Films urls.py

<details><summary>Validator</summary>

![Films urls](documentation/testing/films-urls.png)
</details>

### Films views.py

<details><summary>Validator</summary>

![Films views](documentation/testing/films-views.png)
</details>

## JavaScript Validator  

[JS Hint](https://jshint.com/) was used to test the javascript code.

The validation was completed on all the javascript written for this website. Only the relevant javascript needed is linked to the template that needs it.  
I wanted to try new learning in this project by using JQuery when I could but vanilla javascript was used too when needed. These functions work well but I am aware that the script could possibly be streamlined, this can be looked at at a future date.  
The warnings given are referencing an undefined variable "bootstrap", which is an external libary used.  
See the results functionality and manual testing below.

### base.js  

This comprises of two functions:  

* The first being to timeout the messages. I have manually tested this on all messages and it gives the required timeout result.
* The second function was made to add style to the bootstrap hamburger menu and change the hamburger to an envelope to open and close on click. Manually tested by pressing navbar toggle button and getting the required result.

<details><summary>Validator</summary>

![Base Javascript](documentation/testing/base-js.png)
</details>

### comments.js

This has three functions:

* The first one makes sure the text area on the form is clear once the page is loaded. Manually tested by visiting the member area after editing a comment and all text areas are empty.
* The second function is activated when the 'delete' button is pressed on any comment. It makes the 'delete confirm' button on the modal have the correct href with relevent comment id and slug. Manually tested by pressing the delete buttons, all above above expected outcomes met and works well.
* The last function is activated when the 'edit' button is pressed on any comment. It changes relevent text on the form, puts the form to the correct film value and gives the action the comment id so when the submit button is pressed it goes to the correct view. Manually tested by pressing the edits buttons, all above expected above outcomes met and works well.

<details><summary>Validator</summary>

![Comments Javascript](documentation/testing/comments-js.png)
</details>

### film.js

Here there are two functions:

* The toggle function hides and shows the film information or film poster when the relevent button is pressed. Manually tested by pressing the toggle button and all above expected outcomes met.
* The other function makes sure the youtube video stops playing when the close button on the modal is pressed. Manualy tested by playing trailer and closing, expected outcome of video stopping met.

<details><summary>Validator</summary>

![Film Detail Javascript](documentation/testing/film-js.png)
</details>

## HTML Validator

### Problems/Bugs highlighted and how they were fixed  

* Trailing / on images - Removed to fix issues.
* Multi ID error on full-width-snap-container css ID - Changed to class to fix.
* 'Figurecaption' incorrectly used - Changed to resolve error.
* 'Div' element within 'button' - Changed to span fix error.
* 'frameboarder and aria-labeldby' not needed in iframe - Removed to fix error.
* Attribute 'comment-id' not avaliable for button element - Tis was changed to the attribute 'name'.

### Final Test Results

<details><summary>Home</summary>

![HTML Validator Home](documentation/testing/html-home.png)
</details>

<details><summary>Film</summary>

![HTML Validator Film](documentation/testing/html-film.png)
</details>

<details><summary>Member</summary>

![HTML Validator Member](documentation/testing/html-member.png)
</details>

<details><summary>Error</summary>

![HTML Validator Error](documentation/testing/html-error.png)
</details>

## CSS Validator  

<details><summary>Validator</summary>

![CSS Validator](documentation/testing/css-validator.png)
</details>

### Problems/Bugs highlighted and how they were fixed  

### Final Test Results

## Lighthouse  

### Problems/Bugs highlighted and how they were fixed  

* To improve the performance score each image height and width was added.
* Unnecessary aria labels were removed to improve accessibility scores.

### Final Test Results  

Below are the results of the desktop tests. The mobile results are the same but with lower performance scores due to the time the images take to render.  

<details><summary>Home</summary>

![Lighthouse Home](documentation/testing/lighthouse-home.png)
</details>

<details><summary>Film</summary>

![Lighthouse Film](documentation/testing/lighthouse-film.png)
</details>

<details><summary>Member</summary>

![Lighthouse Member](documentation/testing/lighthouse-member.png)
</details>

<details><summary>Login</summary>

![Lighthouse Login](documentation/testing/lighthouse-login.png)
</details>

<details><summary>Logout</summary>

![Lighthouse Logout](documentation/testing/lighthouse-logout.png)
</details>

<details><summary>Register</summary>

![Lighthouse Signup](documentation/testing/lighthouse-signup.png)
</details>

## Wave  

### Problems/Bugs highlighted and how they were fixed

* Wave suggested underlined text be removed to avoid confusion with link text.  
  Underlined text was removed as per suggestion.  
* The heading of the delete modal skipped the heading level so was altered to fix the issue.
* In the signup template a broken link was found to the login area- this was fixed.

### Final Test Results  

No errors found after final testing.  
There are alerts regarding Redundant links.  
I have considered removing the links mentioned but I have decided to keep them.  
I feel The Logo 'home' link is needed especially in mobile devices when the toggle nav is closed. Extra links to signing up/member-area were added to encourage the user becoming a member and showing the benifits of registering.  

<details><summary>Alert</summary>

![Wave Alerts](documentation/testing/wave-alert.png)
</details>  

## Manual Testing  

## Other Bugs and Errors  

* Images added in the film model CloudinaryField produced an error found in dev tools console stating the image was HTTP instead of the prefered HTTPS.  
This automatically should have been converted to a HTTPS image acording to the cloudinary documention but was not.  
The fix was eventually found in the cloudinary documentation - 'cloudinary.convig secure=true' was added in settings.py which resolved the issue.  
* Once the trailer is played in the film detail page there is a console error due to the embeded Youtube video that can not be fixed at this time. It refers to "ensure CORS response header values are valid". I have researched this and the issue seems to be between Google and Youtube so I am unable to fix this error. This error does not effect the functionality of the site but I plan to research this error more at a future date. This error does not occur if I remove the Youtube iframe. The error can be found below.
  <details><summary>CORS Error</summary>

  ![CORS Error](documentation/testing/cors-error.png)
  </details>
* Linked to the above issue, there are two issues in dev-tools relating to the embeded Youtube iframe form field in the film detail page. This seems to be an external issue with Youtube's iframe. I researched for a fix to this but I could not find one, I will re visit this in the future to see if there is a work around. This error does not occur if I remove the Youtube iframe.
  <details><summary>Youtube Form</summary>

  ![Youtube Form](documentation/testing/youtube-form.png)
  </details>
