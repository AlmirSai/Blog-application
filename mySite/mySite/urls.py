"""Main file for url's, app's url's edit in app folder's
and edit with function include()
"""


from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLResolver


urlpatterns: list[URLResolver] = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog'))
]
