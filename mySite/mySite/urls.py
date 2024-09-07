"""Main file for url's, app's url's edit in app folder's
and edit with fucntion include()
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog'))
]
