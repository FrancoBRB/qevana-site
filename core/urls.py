from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from movieapp.views import *
from seriesapp.views import *
from petitionsapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='HomeView'),
    path('movies/<slug:slug>',MovieDetailView.as_view(),name='MovieView'), 
    path('series/<slug:slug>',CapList,name='CapList'),
    path('series/<slug:slug>/<int:no>',CapView,name='CapView'),
    path('search/',Search,name='Search'),
    path('petitions/', PetitionView, name='PetitionView'),  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
