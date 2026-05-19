
# Movie Sorting App Using Strategy Pattern

Movie Sorting App Using Strategy Pattern is a Django web application that demonstrates how the Strategy Design Pattern can be used to organize and switch between different sorting behaviors in a clean and flexible way.

The app displays upcoming movies and allows the movie list to be sorted using different strategies, such as release date, rating, popularity, and title. Instead of writing all sorting logic directly inside the view, each sorting method is separated into its own strategy class. This makes the code easier to understand, maintain, and expand.

## Project Purpose

The purpose of this project was to practice using the Strategy Design Pattern in a real Django application.

The Strategy Pattern is useful when an application needs multiple ways to perform the same type of action. In this project, the action is sorting movies, and each sorting option is handled by a separate strategy. This shows how design patterns can make code cleaner and easier to modify.

## Features

- Display upcoming movies
- Sort movies by release date
- Sort movies by rating
- Sort movies by popularity
- Sort movies by title
- Uses the Strategy Design Pattern
- Django model for storing movie data
- SQLite database
- Simple HTML template for displaying results

## Why I Built This App

I built this app to demonstrate how the Strategy Pattern works in a simple and practical way.

Instead of using multiple if/else statements inside the view, the project separates each sorting behavior into its own class. This makes the application more flexible because new sorting methods can be added without rewriting the main view logic.

This project helped me understand object-oriented design, clean code organization, and how design patterns can be used inside a Django project.

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Strategy Design Pattern

## How the Strategy Pattern Is Used

The app uses a base strategy class for movie sorting. Different sorting strategies inherit from that base class and define their own sorting behavior.

Examples of sorting strategies include:

- Sort by release date
- Sort by rating
- Sort by popularity
- Sort by title

The Django view selects the correct strategy based on the user's selected sorting option and applies it to the movie list.

## How to Run

To run this project after cloning the repository, follow these steps:

### Clone the Repository

  - cd strategy-pattern
  - python -m venv venv
  - venv\Scripts\activate
  - pip install django
  - python manage.py runserver
