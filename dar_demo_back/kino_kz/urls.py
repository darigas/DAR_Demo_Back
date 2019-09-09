from django.urls import path, include
from .views.movies import *
from .views.cinemas import *

urlpatterns = [
    path('movies', current_movies),
    path('coming_soon_movies', coming_soon_movies),
    path('cinemas', get_cinemas),
    path('cinemas/<city>', get_city_cinemas),
    path('cities', get_cities)
]
