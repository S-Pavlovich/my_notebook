# Схемы URL для orm_app.movie_urls
from django.urls import include, re_path, path
from . import views


urlpatterns = [
    path('', views.all_movie),
    path('<slug:slug_movie>', views.one_movie, name='movie_detail'),
]