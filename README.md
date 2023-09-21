# Works Of Wes Anderson  

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
    - [Languages Used](#languages-used)
    - [Model Structure](#model-structure)
  - [Agile Methodology](#agile-methodology)
  - [Features](#features)
    - [Favicon](#favicon)
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
  - [Content and Media](#content-and-media)

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

### Languages Used

### Model Structure

![Model-Diagram](/documentation/design/works-of-wes-anderson-database-diagram.png)

## Agile Methodology

Please refer to [AGILE.MD](AGILE.md)

## Features

### Favicon

### Accessibility

### Future Implementations

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

### New learning

## Content and Media
