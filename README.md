
# Recipe Sharing Website



This project is a recipe sharing website that allows users to discover and share recipes, comment on them, and rate them. The website is built using Django, BeautifulSoup, and MySQL.


## Technologies Used

The app was built with the following technologies:

- Django: a high-level Python web framework used to build the backend of the website.
- Django Rest Framework: a powerful and flexible toolkit for building Web APIs.
- Paginator: a built-in Django module used to paginate long lists of recipes and ingredients.
- BeautifulSoup: a Python library used to parse HTML and XML documents.
- jQuery: a JavaScript library used to simplify HTML document traversing, event handling, and Ajax interactions.
- Bootstrap: a popular CSS framework used to design responsive and mobile-first websites.
## Features
 #### Models
- Recipe: stores information about the recipes
- Ingredient: stores information about the ingredients used in recipes
- Comment: stores comments made by users about the recipes
- Rating: stores ratings given by users for the recipes

#### Views
- Home page: displays a list of featured recipes
- Recipe page: displays details about a particular recipe
- Ingredient page: displays information about a particular ingredient
- Comment page: displays comments made by users for a particular recipe
- Profile page: displays information about the user's profile
#### Templates
- Recipe template: displays information about a recipe in an attractive layout
- Ingredient template: displays information about an ingredient in an attractive layout
- Comment template: displays comments made by users in an attractive layout
- Authentication and Authorization
- Authentication system: allows users to sign up, log in, and log out
- Authorization system: controls access to comment and rate recipes
#### Search
- Search system: allows users to search for recipes and ingredients
#### Pagination
- Pagination system: divides long lists of recipes and ingredients into smaller pages
#### Web Scraping
- Web scraping script: retrieves information about recipes and ingredients from other cooking sites and imports them into the website
## Diagrams

The project includes use case and class diagrams that meet the functional requirements of the website.
## Getting Started

To run this recipe website locally, follow these steps:
Clone this repository to your local machine using

```bash
    git clone https://github.com/f-amine/Recipes-WebApp.git
```

Navigate to the project directory using

```bash
  cd my-project
```

Install Django, BeautifulSoup, and MySQL

```bash
  npm install BeautifulSoup Django
```

Create a MySQL database
Update the settings.py file with your database credentials

Run the following commands

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```


Open the browser and navigate to

```bash
  http://localhost:8000/
```