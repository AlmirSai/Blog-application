"""App doesn't async architecture, but I don't edit this files"""


import os

from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mySite.settings")

application: ASGIHandler = get_asgi_application()
