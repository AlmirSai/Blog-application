"""App doesn't async architecture, but I don't edit this files"""


import os

from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mySite.settings")

application: WSGIHandler = get_wsgi_application()
