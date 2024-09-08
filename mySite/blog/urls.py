"""File for parsing app's url pattern's"""


from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name: str = 'blog'

urlpatterns: list[URLPattern] = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail')
]
