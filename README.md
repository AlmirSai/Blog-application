# 💻 Blog Application

## A simple blog application built with Django.

Stack:

 Django

Getting Started:

1. Install Dependencies:
   ```bash
   pip install Django
   ```

2. Start Development Server:
   ```bash
   cd django
   python manage.py runserver
   ```
   Note: This project uses a `.env` file to store the `SECRET_KEY` from `settings.py`.  You need to obtain or generate a new secret key to activate the project.

3. Create a Super User:
   ```bash
   python manage.py createsuperuser
   ```
4. You need to generate django key and migrate database

Project Structure:

```
django/
├── blog/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── blog/
│           └── ...
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Features:

 Create, edit, and delete blog posts.
 Manage user accounts.
 Filter posts by status.
 Search for posts.

To-Do:

 Add more features.


Test on:
mac os
