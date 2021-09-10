from django.shortcuts import render
from movieapp.models import *
from seriesapp.models import Serie

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