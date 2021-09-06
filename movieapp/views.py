from django.shortcuts import render
from django.views.generic import DetailView
from .models import Movie


class MovieDetailView(DetailView):
    model = Movie    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        return context

