# Blog Application

## Short describe
This is cross-platform E-commeres Django application
In this project You can create post's, user's and manage your user's and post's

In this project author use .env file for Django key. You need to generate him in .env file

## Comming soon:
```
- tests
- loggging
- production enviroment
```

## Project Structure:

```
mySite/
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

## Getting Started:
THis Roadmap for MacOS user's

1. Install python
   ```bash
   brew install python
   ```
2. Create a Virtual Environment (Recommended):
   ```bash
   python3.12 -m venv .venv  # For this project ,please, use Python 3.12 version minimum 
   source .venv/bin/activate  
   ```

3. Install Dependencies:
   ```bash
   pip install Django
   ```

4. Set up Environment Variables:
   Create a `.env` file in the secrets directory of the project.
   Add the following line to your `.env` file, replacing `your_secret_key` with a secure secret key:
   Directory:
   
   ```
   mkdir mySite/mySite/secrets
   cd mySite/mySite/secrets
   touch .env
   ```
   ```
   mySite/
   ├── mysite/
   │   ├──secrets/
   |       |-.env
   ```
   ```
     SECRET_KEY=your_secret_key
   ```

5. Create a Super User:
   ```bash
   python manage.py createsuperuser
   ```

6. Start Development Server:
   ```bash
   cd mysite
   python manage.py runserver
   ```

## Start project:

```
cd mySite && python manage.py runserver
```

## Testing:
Comming soon. In this project author use:
```
- pylintr
- flake8
- pytest
```

## Deployment:
This project could support in future
Project could place on Yandex Cloud, Selectel and maybe on other cloud services

## To-Do:
For this project author use miro: https://miro.com/app/board/uXjVKhsawVA=/
