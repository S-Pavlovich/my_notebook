from django.shortcuts import render
from orm_app.models import Movie
from django.shortcuts import get_object_or_404
from django.db.models import F


# Create your views here.


def one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie )
    return render(request, 'orm_app/movie_info.html', {'movies': movie})


def all_movie(request):
    movie = Movie.objects.all()
    return render(request, 'orm_app/all_movies.html', {'movies': movie})
