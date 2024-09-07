Getting Started:



1. Create a Virtual Environment (Recommended):
   ```bash
   python3 -m venv .venv  # Create a virtual environment
   source .venv/bin/activate  # Activate the environment
   ```

2. Install Dependencies:
   ```bash
   pip install Django
   ```

3. Set up Environment Variables:
    Create a `.env` file in the secrets directory of the project.
    Add the following line to your `.env` file, replacing `your_secret_key` with a secure secret key:
     ```
     SECRET_KEY=your_secret_key
     ```

4. Start Development Server:
   ```bash
   cd mysite
   python manage.py runserver
   ```

5. Create a Super User:
   ```bash
   python manage.py createsuperuser
   ```

Start project:

```
cd mySite && python manage.py runserver
```

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
│
├── mysite/
│   ├──secrets/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

Testing:

 Framework:  pytest
 Coverage:  ... (Add code coverage report details here)

Deployment:

 Instructions for deploying to Heroku (or your preferred platform).

To-Do:

 Add support for post categories.
 Implement user
