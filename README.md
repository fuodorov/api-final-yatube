# Description

The project is an API for the yatube project.

Functionality:
Authorization by JWT token.

Serialization of data for all project models (Post, Comment, Group, Follow)

# Processing GET, POST, PATCH, PUT and DELETE queries to the Yatube project database

# Installation

## 1)Clone the repository
## 2)Create and activate virtual environment for the project

`python -m venv venv`

`source venv/scripts/activate`

## 3)Install dependencies

`python pip install -r requirements.txt`

## 4)Make migrations

`python manage.py makemigrations`
`python manage.py migrate`

## 5)Run the server

`python manage.py runserver`

## Examples.

In order to access the API you need to get a token:
You need to make a POST request to `localhost:8000/api/v1/token/` by passing username and password fields. The API will return the JWT-token

Next, by passing the token you will be able to access the methods, e.g:

`/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)`

When sending a request, pass a token in the Authorization: Bearer <token> header

The word Bearer here replaces the word Token and means that it is followed by the token itself.
