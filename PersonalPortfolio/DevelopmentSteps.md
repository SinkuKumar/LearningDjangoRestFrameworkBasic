# Personal Portfolio - Development Steps

## Getting Started

1. **Create and activate a virtual environment:**  
    - `python3 -m venv venv`
    - `venv\Scripts\activate`
2. **Install Django:**  
    - `pip install django`
3. **Install Django REST framework:**  
    - `pip install djangorestframework`
4. **Create a new Django project:**
    - `django-admin startproject PersonalPortfolio`
    - `cd PersonalPortfolio`
    - `python manage.py runserver`
5. **Create a new Django app:**
    - `python manage.py startapp portfolio`
    - Add the app to the `INSTALLED_APPS` list in the `settings.py` file.
6. **Create a new Django model:**
    - Define the model in the `models.py` file.
    - `python manage.py makemigrations`
    - `python manage.py migrate`
7. **Create a new Django serializer:**
    - Define the serializer in the `serializers.py` file.
8. **Create a new Django view:**
    - Define the view in the `views.py` file.
9.  **Create a new Django URL pattern:**
    - Define the URL pattern in the `urls.py` file.
10. **Create a new Django template:**
11. **Create a new Django form:**
12. **Create a new Django admin:**
13. **Create a new Django migration:**
14. **Create a new Django superuser:**
15. **Run the Django development server:**