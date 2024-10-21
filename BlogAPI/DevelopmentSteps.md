# BlogAPI - Development Steps

## Getting Started

1. **Create and activate a virtual environment:**  
    - `python -m venv venv`
    - `venv\Scripts\activate`
2. **Install Required Packages:**  
    - `pip install django`
    - `pip install djangorestframework`
3. **Create a new Django project:**
    - `django-admin startproject BlogAPI`
4. **Create a new Django app:**
    - `python manage.py startapp blog`
    - Add the `blog` and `rest_framework` app to the `INSTALLED_APPS` list in the `settings.py` file.
    - Add the `rest_framework` app to the `DEFAULT_AUTHENTICATION_CLASSES` and `DEFAULT_PERMISSION_CLASSES` lists in the `settings.py` file.
5. **Create the models for the blog app:**
6. **Create the serializers for the blog app:**
7. **Create the views for the blog app:**
8. **Create the URLs for the blog app:**
9. **Run the server:**
    - `python manage.py runserver`
10. **Generte fake data:**
    - `python manage.py generate_data`