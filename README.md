# Favourite Movie App

This is a simple application that allows you create and see a list of movies with a few other meta data using django

## Installation

* __Install Python3 from python.org__ 
* __Create a virtual environment__

* __Install dependencies__
 
```bash
pip install requirement.txt
```

UI Sample
* Home
![Alt](/home.png "Home Page")
 
* List 
![Alt](/molist.png "List of Movies")  

* Create Movies
![Alt](/mocreate.png "Create Movies")

## Usage

```bash
python manage.py runserver
```
Access the home page

```http
http://localhost:8000
```

## Validation
Using Django forms forms must be valid before any commit will happen. Except for special validations like comparing two passwords or anything else which can also be handled in the clean method but this task doesn't require any of such parameters so it's absent.

However, if you enter an invalid parameter it'll not throw a validation error and show you a nice error message. And with some html5 syntax it will not allow you to submit required input values without filling them out. But if someone changes that via inspect, the server will still catch it.

## License
[MIT](https://choosealicense.com/licenses/mit/)