"""App doesn't async architecture, but I don't edit this files"""


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mySite.settings")

application = get_asgi_application()
