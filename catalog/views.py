from django.forms.utils import pretty_name
from django.shortcuts import render
from movieapp.models import Genres,Movie
from seriesapp.models import Serie
from .forms import AdvancedSearchForm
from django.db.models.query_utils import Q

def CatalogView(request):
    genre_list = Genres.objects.all()
    form = AdvancedSearchForm()
    context = {
        'genres':genre_list,
        'form':form,
    }
    if request.method=="POST":
        form=AdvancedSearchForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data            
            searched_year=content['Año']
            searched_genre=content['Genero']
            searched_type= content['Tipo']
            if searched_type == '2':
                results = Movie.objects.filter(Q(date__contains=searched_year) & Q(genres__genre_name=searched_genre))
                type_searched = 'movies'
            else:
                results = Serie.objects.filter(Q(date__contains=searched_year) & Q(genres__genre_name=searched_genre))
                type_searched = 'series'
            searched_ops= {
                'results':results,
                'type':type_searched,
            }
            return render(request,'advanced_search.html',searched_ops)
        else:
            form = AdvancedSearchForm()
    return render(request,'catalog.html',context)

def GenreView(request,pk):
    genre_list = Genres.objects.filter(pk=pk)
    searched_genre = genre_list.first()
    genre_series = Serie.objects.filter(genres__genre_name=searched_genre.genre_name)
    genre_movies = Movie.objects.filter(genres__genre_name=searched_genre.genre_name)
    context = {
            'genre':searched_genre,
            'movies_founded':genre_movies,
            'series_founded':genre_series
    }
    return render(request,'genres.html',context)