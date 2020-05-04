from django.conf.urls import url
from django.urls import path
from . import views as movie_views

urlpatterns = [
    path('', movie_views.homepage, name='home'),
    path('search', movie_views.serach_movie, name='search-movie'),
]