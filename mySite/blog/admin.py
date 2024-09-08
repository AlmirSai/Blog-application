"""File for access control for admins"""


from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Class for controlling postings"""
    list_display: list[str] = ['title', 'slug', 'author', 'publish', 'status']
    list_filter: list[str] = ['status', 'created', 'publish', 'author']
    search_fields: list[str] = ['title', 'body']
    prepopulated_fields: dict[str, tuple[str]] = {'slug': ('title',)}
    raw_id_fields: list[str] = ['author']
    date_hierarchy: str = 'publish'
    ordering: list[str] = ['status', 'publish']
