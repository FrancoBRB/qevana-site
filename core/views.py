from django.db.models.query_utils import Q
from django.shortcuts import render
from movieapp.models import *
from seriesapp.models import Serie
import string

def HomeView(request):
    rec_movies = Movie.objects.filter(recommended=True)
    prem_movies = Movie.objects.filter(premiere=True)
    rec_series = Serie.objects.filter(recommended=True)
    context = {
        'rec_movies':rec_movies,
        'prem_movies':prem_movies,
        'rec_series':rec_series,
    }
    return render(request,'index.html',context)

def Search(request):
    if request.method == 'POST':
        searched = request.POST['search-bar'].capitalize()        
        movie_db = Movie.objects.filter(Q(title__contains=searched) | Q(alt_title__contains=searched))
        series_db = Serie.objects.filter(Q(title__contains=searched) | Q(alt_title__contains=searched))
        context = {
            'searched':searched,
            'movies_founded':movie_db,
            'series_founded':series_db
        }
        return render(request,'search.html',context)
    else:
        return render(request,'search.html',{})

   