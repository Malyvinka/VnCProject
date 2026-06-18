# Vanitas no Carte API

A simple REST API and web project built with Django and Django REST Framework.

Inspired by foxapi.dev and based on the world of **The Case Study of Vanitas (Vanitas no Carte)**.

## Features

* Character database
* Pagination
* Django REST Framework
* Responsive dark theme
* JSON-style cards
* API endpoints

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* HTML/CSS

## Installation

Clone the repository:

```bash
git clone https://github.com/Malyvinka/VnCProject.git
```

Go to the project folder:

```bash
cd VnCProject
```

Install dependencies:

```bash
pip install django djangorestframework
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

## API Endpoint

### Get all characters

```
GET /api/characters/
```

Example response:

```json
[
  {
    "id": 1,
    "name": "Vanitas",
    "species": "human"
  }
]
```

## Future Plans

* Character detail page
* Search
* Filtering
* Ordering
* PostgreSQL support
* Docker support
* Swagger/OpenAPI documentation

## License

This project is created for educational purposes.

Inspired by *Vanitas no Carte* by Jun Mochizuki.

```
```
