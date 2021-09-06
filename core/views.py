from django.shortcuts import render
from movieapp.models import *

def HomeView(request):
    rec_movies = Movie.objects.filter(recommended=True)
    prem_movies = Movie.objects.filter(premiere=True) 
    context = {
        'rec_movies':rec_movies,
        'prem_movies':prem_movies
    }
    return render(request,'index.html',context)