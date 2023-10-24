# Works Of Wes Anderson  

![Responsive](/documentation/design/responsive.png)

Visit the deployed site: [Works-Of-Wes-Anderson](https://works-of-wes-anderson-b656acb2e110.herokuapp.com/)

Works Of Wes Anderson is a website made to celebrate the films of Wes Anderson.  
The website's fun and clear design shares information on each film along with positive comments from both critics and visitors.  
Members can sign in, have their say and rate the qualities of each film.

## CONTENTS

- [Works Of Wes Anderson](#works-of-wes-anderson)
  - [CONTENTS](#contents)
  - [User Experience](#user-experience)
    - [Who is the Website for](#who-is-the-website-for)
    - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Images and Icons](#images-and-icons)
    - [Wireframes](#wireframes)
      - [Navigation Bar](#navigation-bar)
      - [Home Page](#home-page)
      - [Film Detail](#film-detail)
      - [Member Area](#member-area)
    - [Model Structure](#model-structure)
      - [Film model](#film-model)
      - [Critic Comment Model](#critic-comment-model)
      - [Member Comment Model](#member-comment-model)
      - [Score Model](#score-model)
  - [Agile Methodology](#agile-methodology)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks Libaries and Programs Used](#frameworks-libaries-and-programs-used)
  - [Features](#features)
    - [Nav Bar](#nav-bar)
    - [Footer](#footer)
    - [Home](#home)
    - [Film Detail](#film-detail-1)
    - [Member Area](#member-area-1)
      - [Each Film](#each-film)
      - [Add Comment and Rating](#add-comment-and-rating)
      - [Edit Comment](#edit-comment)
      - [Delete Comment and Rating](#delete-comment-and-rating)
    - [Log In/Out/Register](#log-inoutregister)
    - [Messages](#messages)
    - [Error Pages](#error-pages)
    - [Favicon](#favicon)
    - [Scroll Container](#scroll-container)
    - [Accessibility](#accessibility)
    - [Future Implementations](#future-implementations)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Fork Repository](#fork-repository)
    - [Clone Repository](#clone-repository)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Learning](#learning)
    - [New learning](#new-learning)
  - [Media](#media)

## User Experience

### Who is the Website for

The site is primarily for fans of Wes Anderson to celebrate his works, have thier say and enjoy other peoples views.  
It can also be for users new to Wes Anderson's work to come and find out more.  
The site also encourages return visitors by offering a registration service where they can comment and score the different qualities of each film.

### Design

Wes Anderson is known for his unique visual style. He likes using symmetry, beautiful color pallets and huge attention to detail.  
This website is not trying to emulate Wes Anderson's style because that is not possible, but it does take elements of his design choices.  
Wes Anderson sticks with a clear design theme throughout his films and usualy has a retro feel to them. This website is the same and has a simple retro, newspaper design that runs throughout and uses symmetrical layouts.

### Colour Scheme

The color scheme fits in with the overal design goals.  
Black text on a White background is used to keep to the simple, retro, newspaper theme and it also ensures the contrast is up to WCAG standards.  
Each film has a unique color scheme, this site utilises them by using two of the colors from each film within the appropriate film's section. A color picker tool was used on images from the film to pick the two colors.  
Below are the colors used for each element of the website.

![Color-Pallet](/documentation/design/works-of-wes-anderson-color-pallet.png)

### Typography

The choice of Typography again follows the retro, newspaper theme. Special-Elite from [Google Fonts](https://fonts.google.com/specimen/Special+Elite) was used throughout to replicate a typewrite style.

![Special-Elite](/documentation/design/special-elite-font.png)

### Images and Icons

With the deliberately minimal design layout, typography and color scheme the icons are very important to make sure the site is visualy appealing. These icons are in keeping with the websites style, many of them are drawings related to Wes Anderson films. The icons were purchased from [The-Noun-Project](https://thenounproject.com/).  
Each film has one image, it's poster. A more unique poster was chosen to add interest, the posters are from [The-Poster-DB](https://theposterdb.com/).

### Wireframes

#### Navigation Bar

![Navigation-Bar-Wireframe](/documentation/design/navigation-bar.png)

#### Home Page

![Home-Page-Wireframe](/documentation/design/home.png)

#### Film Detail

![Film-Detail-Wireframe](/documentation/design/film-detail.png)

#### Member Area

![Member-Area-Wireframe](/documentation/design/member-area.png)

### Model Structure  

Below is the model structure of the website.  

![Model-Diagram](/documentation/design/works-of-wes-anderson-database-diagram.png)  

#### Film model  

This is for the Admin to add a new Wes Anderson film.  
All fields are required except the color class and icons. If these are not given default colors and icons will be used.  
The Trailer link was taken from the film's Youtube embed link, the posters from The [The-Poster-DB](https://theposterdb.com/) and icons from [The-Noun-Project](https://thenounproject.com/).

#### Critic Comment Model  

This is for the Admin to add critic comments for each film, it has a film field as a foriegn key for the film commented on.  

#### Member Comment Model  

This is for a member to add a comment for each film, it has foriegn keys for each film and user.  
Each comment has an approved setting which is set to false until the admin approves it.  

#### Score Model  

This is for a member to add a rating for each film, it has foriegn keys for each film and user.  
Each category of rating has a choice of 1-5.  

## Agile Methodology

Please refer to [AGILE.MD](AGILE.md)  

## Technologies Used  

### Languages Used  

- HTML
- CSS
- Javascript
- Python

### Frameworks Libaries and Programs Used  

- Git - Used for version control
- GitHub - Used to store the repository and GitHub projects for the Kanban board
- Django - Used as the framework
- Codeanywhere - Used as the development environment
- Jinja - Template engine for Python
- Bootstrap - Used to help build a responsive website
- Jquery - Used to help create the javascript functions
- Django allauth - Used for account registration
- Django crispy forms - Used to display forms
- Cloudinary - Used to store and serve images
- [ElephantSQL](https://www.elephantsql.com/) - Used for the database
- [Google Fonts](https://fonts.google.com/) - Used for the font
- [balsamiq](https://balsamiq.com/) - Used to create wireframes
- [lucid](https://lucid.app/) - To create model diagrams

## Features

### Nav Bar  

![Navigation Bar Large](/documentation/features/nav-large.png)  

![Navigation Bar Small](/documentation/features/nav-small-open.png)

### Footer  

![Footer](/documentation/features/footer.png)

### Home  

![Home](/documentation/features/home-medium.png)

### Film Detail  

![Film Detail](/documentation/features/film-detail-large.png)

### Member Area

#### Each Film  

![Member Area Film Section](/documentation/features/member-film.png)

#### Add Comment and Rating  

![Add Comment and Rating](/documentation/features/add-comment-rating.png)

#### Edit Comment  

![Edit Comment](/documentation/features/edit-comment-small.png)

#### Delete Comment and Rating  

![Delete Comment and Rating](/documentation/features/delete-comment-rating.png)  

![Delete Comment Modal](/documentation/features/delete-modal.png)

### Log In/Out/Register  

![Register](/documentation/features/register-small.png)

### Messages

### Error Pages  

![Error Pages](/documentation/features/error-small.png)

### Favicon  

A Favicon was created for this website at [Favicon.io](https://favicon.io/).

![Responsive](/documentation/design/favicon-example.png)  

### Scroll Container  

The horizontal scroll container is used throughout this website containing the comments and having custom scroll bar colors matching the relevant film.  
This feature was choson as it fits in well with the newspaper/retro style. I also feel that it works well on mobile devices as peolple are used to swiping and scrolling whilst using other popular social media websites.  
It has been mentioned that this typle of horizontal scroll isn't usually used with website content and it might not apeal everyone. I can see this point of view but decided to stick with the initial style choice and kept them in.

### Accessibility  

- The accessibility of the website was tested by both Wave and Lighthouse (score of 100), please see the [TESTING page](TESTING.md) page for details.  
- All the images have relevant alt descriptions.  
- The link to wikipedia opens in a new tab.
- The buttons have clear hover effects and also have a focus effect for keyboard users.

### Future Implementations  

This is the first release of this website that meets the scope of this project. As seen in the [AGILE page](AGILE.md) and the project [Issues](https://github.com/DavidDock/works-of-wes-anderson/issues) there are remaing issues for future implementations.  
I would like to improve the benefits to becoming a member. At the moment the benefits are being able to contribute to the website and make your opinion known by commenting and rating a film.  
I would like the member to feel more connected to the website by being able to create a profile with added functionality like naming and changing their favorite film and having a watch list of Wes Anderson films and also have the ability to view other members profile.  
Another fantasic idea given to me by my mentor was adding a quiz to the website. I think that this idea would take the website to the next level.

## Deployment  

### Heroku

This site was deployed using Heroku via GitHub and developed using codeanywhere. The following steps were followed to deploy the site:

- Makesure the development environment has:
  - All the requirements are up to date in requirements.txt
  - The settings.py is set up to use DATABASE_URL(ElephantSQL used for this project's database), CLOUDINARY_URL  (Used for hosting images uploaded) and SECRET_KEY (Django secret key), all pointing to the env.py where the environment variables are stored or will be found in Heroku convig vars when deployed
  - An env.py file storing sensitive keys for Django (Secret_key), Database( ElephantSQL) and image storage (Cloudinary_url)
  - The static configuration is correct (In this project Cloudinary used for media and Whitenoise used to serve static)
  - A Procfile added with web: gunicorn project_name(worksofwes).wsgi
  - Debug set to only true in development mode
  - All migrations are made
  - All changes commited and pushed to GitHub where the repository is stored
- Log in to Heroku and create App with unique name
- Add following convig Vars to new App:
  - DATABASE_URL with database value in env.py (Copied from the relevant ElephantSQL database instance)
  - SECRET_KEY with django secret key value in env.py (Create this yourself)
  - PORT to 8000
  - CLOUDINARY_URL with cloudinary value in env.py (Copied from API environment variable in Cloudinary account)
- Add Heroku url to Allowed hosts in settings.py file and push this to GitHub
- Click on deploy and choose GitHub and link to the repository ([Works-Of-Wes-Anderson-GitHub-Repository](https://github.com/DavidDock/works-of-wes-anderson))
- Click on deply branch
- Open App

Visit the deployed site: [Works-Of-Wes-Anderson](https://works-of-wes-anderson-b656acb2e110.herokuapp.com/)

### Fork Repository

- Go to the [Works-Of-Wes-Anderson-GitHub-Repository](https://github.com/DavidDock/works-of-wes-anderson) repository
- Click "Fork" which can be found in the top right corner

### Clone Repository

- Go to the [Works-Of-Wes-Anderson-GitHub-Repository](https://github.com/DavidDock/works-of-wes-anderson) repository
- Under the repository click on "go to" then under the "local" tab copy the HTTPS clone URL
- In your local development environment go to the terminal
- Change the current working directory to the location you want the cloned directory to be made
- Type "git clone" and then paste the clone URL and press enter

## Testing

Please refer to [TESTING.MD](TESTING.md)  

## Credits  

### Learning  

The code used for this project was taught to me by code insitute. The Code Insitutes project run through 'I think therefor i blog' helped me greatly with the development of my project.

### New learning  

The use of context-processors was Learnt from [djangocentral.com](https://djangocentral.com/how-to-create-custom-context-processors-in-django/)

The use of scroll containers was learnt from [Kevin Powell](https://www.youtube.com/watch?v=3yfswsnD2sw)  

For highlighting active links learnt from [valerymelou.com](https://valerymelou.com/blog/2020-05-04-how-to-highlight-active-links-in-your-django-website)

Reading the official documentaion for django and cloudinary was useful for many elements of this website including having a min and max validation for the model.

## Media

- [Tinypng.com/](https://tinypng.com/) - Used to compress images
- [Cloudconvert.com](https://cloudconvert.com/webp-converter) - Used to convert images to webp
- [Favicon.io](https://favicon.io/) - Used to generate favicon
- [Amiresponsive](https://ui.dev/amiresponsive) - Used to see site on different devices and get image for the top of this README
- [The-Noun-Project](https://thenounproject.com/) - Used for the icons
- [The-Poster-DB](https://theposterdb.com/) - Used for the film posters
