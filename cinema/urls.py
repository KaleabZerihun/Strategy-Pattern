
from django.urls import path
from .views import upcoming_movies

urlpatterns = [
    path("", upcoming_movies, name="upcoming_movies"),
]
