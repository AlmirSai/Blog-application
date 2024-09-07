"""Config file for app 'blog'"""


from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Config class"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
