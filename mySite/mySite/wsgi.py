"""App doesn't async architecture, but I don't edit this files"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mySite.settings")

application = get_wsgi_application()
