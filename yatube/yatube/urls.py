from django.contrib import admin
from django.urls import include, path

"""yatube URL Configuration"""

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls)
]
