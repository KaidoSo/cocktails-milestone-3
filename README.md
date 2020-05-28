<h1 align="center">
Data Centric Development - Milestone Project 3 - DrinkUs by Kaido Soomlais
</h1>

<div align="center">
    <img src="https://raw.githubusercontent.com/KaidoSo/cocktails-milestone-3/master/static/images/drinkus-image.png" href="https://kaidoso-drinkus.herokuapp.com/" target="_blank" alt="" border="0">
</div>

[DrinkUs](https://kaidoso-drinkus.herokuapp.com/) is a website created for storing various cocktail recipes in MongoDB. It has been made so that user can easily read & navigate around the website.
Functionality has been added to allow viewing, creating, editing and deleting recipes.
<br><br>

<h1>Table of Contents</h1>

1. [**UX**](#ux)
    - [**Project Purpose**](#project-purpose)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design Choises**](#design-choises)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
        - [Encrypted Login](#encrypted-login)
        - [Context Sensitive NavBar](#context-sensitive-navbar)
        - [Context Sensitive Buttons](#context-sensitive-buttons)
        - [Error Handling](#error-handling)
    - [**Features Left to Implement**](#features-left-to-implement)
        - [Favourites](#favourites)
        - [Search](#search)
        - [Pagination](#pagination)
        - [Forgot Password](#forgot-password)
3. [**Testing**](#testing)
    - [**Tools and Methods For Testing**](#tools-and-methods-for-testing)
        - [HTML](#html)
        - [CSS](#css)
4. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choise)
    - [**Data Types**](#data-types)
    - [**Collection Structure**](#collection-structure)
        - [Users Collection](#users-collection)
        - [Recipes Collection](#recipes-collection)
5. [**Bugs**](#bugs)
    - [**Bugs During Development**](#bugs-during-development)
    - [**Known Bugs**](#known-bugs)
6. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Frameworks/Libraries**](#frameworks-libraries)
    - [**Software**](#software)
    - [**Additional Recources**](#additional-recources)
7. [**Deployment**](#deployment)
    - [**Deployment to Heroku**](#deployment-to-heroku)
    - [**Running this project locally**](#running-this-project-locally)
8. [**Credits**](#credits)
    - [**Acknowledgements**](#acknowledgements)
    - [**Guidance**](#guidance)
9. [**Disclaimer**](#disclaimer)




The main objective in creating the DrinkUs application is to provide the user with a simple to use repository of recipes for cocktail and drink making. It also provides an ever growing database of cocktails, drinks, and ingredients for the users to browse through and add to.
This application is designed with adventurous drinkers in mind who require an easy way to explore drinks menu based on what they might have on hand, or discover a new drink they may not have tried before.
As a side goal, I have left room for expansion once I have developed my skills further. I would like to develop this into a more viable website with added features as outlined below in the [**Features Left to Implement**](#features-left-to-implement).


## UX

#### Project Purpose

- Registration
- Log In
- Viewing cocktails
- Creating a recipe
- Editing a recipe
- Deleting a recipe
- Creating an ever expanding database project that users can easily add to, and over time will grow to large repository of information on drink creation.

### User Stories

 **I want for a user to have:**
 1. A website that is easy to navigate.
 2. A website which is pleasant to look at.
 3. A way to edit and delete my own recipes.
 4. An application which makes it easy to edit my own recipes.
 5. An application that makes it possible for only myself to change my own recipes.
 6. An application that is fast, with very short load times.
 7. A page that I can easily add my own creations to.

### Wireframes

Wireframes were built in the early stages of development to get a rough outline of the structure needed for the planned features of the site. These can be viewed below:

- [Desktop](https://raw.githubusercontent.com/KaidoSo/cocktails-milestone-3/master/static/images/Wireframes1.png)
- [Desktop Drink View](https://raw.githubusercontent.com/KaidoSo/cocktails-milestone-3/master/static/images/Wireframes2.png)
- [Mobile](https://raw.githubusercontent.com/KaidoSo/cocktails-milestone-3/master/static/images/Wireframes3.png)

### Design Choices

The main approach to this application is made to easy to maintain, and easy to use database. To provide features that make the entire experience simple. The following design choices were made to reflect this:

**Fonts**

- The main body font **Gotu** was chosen due to it's simplistic yet fun design.

**Colours**

- The colour choices were made to be simplistic, but to constrast the images presented in the drinks.
- Colours of **steel grey** and **white** were chosed to not overload the user, and maintain a simple, clean look.

**Styling**

- **Bootstrap** framework was used to keep the site simple, only displaying relevant information, without drawing attention away from the content.
- **Buttons** have been styled with bootstrap & colors have been picked using bootstrap color shceme.


## Features

### Existing Features

1. **Encrypted Login**
    - A login form comes with encryption using the bcrypt system in Python. This ensures that any sensitive data passed to the database is encrypted using a salt, which is then tied to that user.
    - This encrypted login system is also tied to the registration form, which is ecrypted before posting to the database.

2. **Context Sensitive NavBar**
    - The navbar has been created to change from a Login button, to Logout button once they are logged in.
    - Logging in also gives the user an option to Create a recipe.

3. **Context Sensitive Buttons**
    - When viewing a drink, by default, the page only generates the drink information.
    - If a user is logged in, and if the user is the person who created the document, they are then presented with the edit drink, and delete drink buttons. Delete drink having an extra confirmation to avoid accidental deletion.

4. **Error handling**
    - A system is in place should a user try to access the add drinks page, and they are not logged in.
    - Should a user try the above, they will be immediately redirected to the login page. This also occurs with any registered user only features.
    - Error handling on the ingredients search is also handled by checking if method is POST. Should no ingredient be entered, but method is not POST, it will return the standard page. If method is POST, it will generate content for "No Ingredients Found".

### Features Left to Implement

1. **Favourites**

I would like to impliment a system that allows the user to favourite a drink, then return all drinks on a favourites page that the user has favourited.

2. **Search**

A search function for user to enter keywords and finding drinks based on them.

3. **Pagination**

Current website would get very cluttered without pages. I want to add that option for a user to view different pages of recipes.

4. **Forgot Password**

Current link doesn't have a function behind it.


## Testing

### Tools and Methods Used for Testing

- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

Both virtual and real device tests were run to test and access the functionality of the app and identify any potential errors. Although the app UI aesthetics are not 
a high priority requirement for this project, the app responsiveness was also tested by resizing the window. Below is a full list of devices used in the testing phase:

Simulated with Chrome DevTools:
Moto G4
Galaxy S5
Pixel 2
Pixel 2 XL
iPhone 5/SE
iPhone 6/7/8
iPhone 6/7/8 Plus
iPhone X
iPad
iPad Pro

Physical Devices:
Samsung Galaxy S8
Sony Xperia XZ1 Compact
Lenovo ThinkBook M-14 IML

Tested Sections HTML CSS:
 - Links to navigate within website and code authors GitHub repository.
 - Checked button sizes so, they were responsive and large enough to be clicked.
 - Spell checked all text content.
 - HTML and CSS validation via w3.org (only Bad Value errors with {url_for} links remained).
 - Created several users and added, edited and deleted cocktails with and without pictures, with and without intentional input errors during filling out the forms.


## Information Architecture

### Database Choice

A NoSQL database was chosen, MongoDB in particular to suit the needs of storing user information and recipes.

### Data Types

The types of data in this project stored in MongoDB are:
- ObjectId
- String
- Binary

### Collections Structure

DrinkUs relies on two connected database collections:

### Users Collection
| Title         | Key in db | form validation type | Data type |
|---------------|-----------|----------------------|-----------|
| Username ID   | _id       | text, Length         | ObjectId  |
| Username      | username  | text                 | String    |
| Password      | password  | text                 | Binary    |
| Email Address | email     | email                | String    |

- Passwords are entered as string, but stored as binary after encryption. The same process is carried our when logging in. The supplied password is encrypted using the supplied key in the password section, and checked to match the existing encrypted binary password.

### Recipes Collection
| Title               | Key in db      | form validation type | Data type |
|---------------------|----------------|----------------------|-----------|
| Drink ID            | _id            | None                 | ObjectId  |
| Drink Name          | name	       | text                 | String    |
| Created By Username | user           | None                 | String    |
| Drink Image URL     | drinkImage     | url                  | String    |
| Ingredients         | ingredients    | textarea             | String    |
| Instructions        | instructions   | textarea             | String    |


## Bugs

### Bugs During Development

Testing for end user experience was done by myself.

1. **Images not rendering**
    - **Issue:** Users tried to add images to their creations. As they were not familiar what type of link was needed, the site would then render a broken image link, causing surrounding elements to shift out of place.
    - **Solution:** Added jQuery function to check page for errors on images. Should it find an error in an image link, it would replace the image source with a predefined standard image link, with the text "No Image Available" inside.
    - **Result:** Function detected errors and corrected the issue. All sibling elements then rendered correctly around the broken image.

2. **Any user could delete/edit**
    - **Issue:** Buttons to edit and delete drinks were available to all users regardless if they added the item or not.
    - **Solution:** Impliment user specific buttons, and encrypted logon system. 
    - **Result:** Users are now only presented with buttons that apply to their own drinks, preventing others from deleteing their creations, and preventing a user stumbling across the site, and removing the entire database.

### Known Bugs

- **Drinks List on Mobile**
In Mobile view the long names for drinks may look a bit off by name crawling up next to the image of the drink. I will look into fixing that in the future when implementing pagination and possibly rehauling the whole home page view.


## Technologies Used

### Languages:
- [Python](https://www.python.org/)
    - The project uses **Python** to run the application.
- [HTML](en.wikipedia.org/wiki/HTML)
    - The project uses **HTML** to structure the DOM.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** to style and theme pages..
 - [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - The project uses **Javascript** to allow for DOM manipulation.

### Frameworks/Libraries:  
- [JQuery](https://jquery.com)
    - **JQuery** is used to simplify DOM manipulation.            
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
    - **Flask** is used to dynamically generate pages, generate dynamic links, and content within the application.
- [PyMongo](https://api.mongodb.com/python/current/)
    - **Pymongo** is used to initiate a connection with, and transfer data to and from MongoDB.
- [Materialize](https://bootstrap.com/)
    - **Bootstrap** is used framework to simplify the structure of the website and make the website responsive easily.
- [MongoDB](https://www.mongodb.com/)
    - **MongoDB** is used to store all project documents within an easily accessible database.
- [Bcrypt](https://www.npmjs.com/package/bcrypt)
    -  Bcrypt library is used to encrypt passwords for user security.

### Software:
- [GitPod](https://www.gitpod.io/)
    - **GitPod** is used to create all files contained in the site, and push to GitHub.

### Additional Resources:    
- [Google Fonts](https://fonts.google.com/)
    - **Google fonts** are used to style the website fonts.
- [Font Awesome](https://fontawesome.com/)
    - **Font Awesome** is used to style additional website icon links.
- [HTML Validator](https://validator.w3.org/)
    - This project utilised the HTML validator provided by W3C to check and correct any issues in my current HTML code.


## Deployment

This project was developed using [GitPod](https://www.gitpod.io/) , [Python](https://www.python.org/) and committed to repository and pushed to [GitHub](https://github.com/KaidoSo/cocktails-milestone-3) using Git options in GitPod.

The main method of deployment is [Heroku](https://kaidoso-drinkus.herokuapp.com/), connected directly to my [GitHub Repository](https://github.com/KaidoSo/cocktails-milestone-3), and deployed within the [Heroku Dashboard](https://www.heroku.com/).

### Deployment to Heroku

To deploy this page to [Heroku](https://www.heroku.com/) from its [GitHub repository](https://github.com/KaidoSo/cocktails-milestone-3), the following steps were taken: 
1. Log into [Heroku](https://dashboard.heroku.com/). 
2. From the main dashboard, select the **New** dropdown, then select **Create new app**.
3. Give your app a unique name, and select the region you wish to deploy to.
4. After the app is created, select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
5. Select **GitHub** as the method of deployment.
6. Log in using your **Github credentials.** 
7. Select your username, and search for the reposity in the **repo-name** box.
8. Select **Connect** on the repository you wish to connect to.
9. Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**
10. After the application is built, select **Settings** from the top of the page.
11. Select **Reveal Config Vars**.
12. Add the config keys for **IP**, **PORT**, **MONGO_URI**, **MONGO_DBNAME**, and **SECRET_KEY** (These will not be published here for security reasons).
13. Select **More** from the top right of the page, and select **Restart all dynos**.


### Running this project locally

**Please note: This project was created and run on Windows in GitPod using Python 3 and Git. Please ensure you have Python 3 installed in your GitPod before running this project. For other OS or Code Editors, please refer to the relevant documentation for your enviroment.**

**Preferred Requirements:**  
 - [GitPod](https://www.gitpod.io/)
 - [Python](https://www.python.org/)
 - An account with [MongoDB Atlas](https://www.mongodb.com/) or a local instance of MongoDB. Please refer to the [MongoDB Documentation](https://docs.atlas.mongodb.com/) for more help.

To clone this project from GitHub:

For help on cloning a repository on Github, please click [here](https://help.github.com/en/articles/cloning-a-repository).


## Credits

### Acknowledgements

Code for structure and layout was partially inspired by the [Corey Schafer YouTube Channel](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)

#### Guidance

I received some advice on tehcnical aspects with this project from Tutor group in Code Institute when getting stuck and unable to reach solution on my own.
Mentored by Spencer Barriball.


## Disclaimer

Please note that all code and images in this site are for educational purposes only. Created only to show my abilities in the language of Python/Flask. 