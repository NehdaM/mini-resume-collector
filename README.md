# Mini Resume Collector API

A simple Django REST Framework project to collect resume details via API, store them temporarily in memory without using a database

## Features

- Accepts resume details(name, email, phone number)
- Input validation using DRF serializers
- Temporary data storage
- REST endpoints for creating , deleting and retrieving resumes

## Technologies Used(Version)

- Python 3.12
- Django 6.0.2
- Django Rest Framework 3.16.1

## Installation steps

1. Clone repository
2. Create virtual environment
    python -m venv venv
    
    To activate virtual environment:
    # Windows
    venv\Scripts\activate
    # mac
    source venv/bin/activate    

3. Install Dependencies
    pip install -r requirements.txt

## Run the app

1. Run Django server
    python manage.py runserver

2. Server starts at
    http://127.0.0.1:8000/

3. Endpoints
    - GET       -   /health/
    - GET       -   /api/resumes/
    - GET       -   /api/resumes/<id>/
    - POST      -   /api/resumes/
    - DELETE    -   /api/resumes/<id>/


## Example API Requests

1. Create a Resume
Endpoint: /api/resumes/
Method: POST
BODY:
request-
{
    "name": "test",
    "email": "test@gmail.com",
    "ph_no": "9876543219"
}

response-
{
    "message": "Resume Created Successfully!",
    "data": {
        "name": "test",
        "email": "test@gmail.com",
        "ph_no": "9876543219",
        "id": 1
    }
}

2. Get all Resumes
Endpoint: /api/resumes/
Method: GET
BODY:
response-
[
    {
        "id": 1,
        "name": "test",
        "email": "test@gmail.com",
        "ph_no": "9876543219"
    }
]

3. Get Resume by Id
Endpoint: /api/resumes/1/
Method: GET
BODY:
response-
{
    "id": 1,
    "name": "test",
    "email": "test@gmail.com",
    "ph_no": "9876543219"
}