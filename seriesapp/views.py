from django.shortcuts import render
from .models import Caps, Serie

def CapList (request,slug):
    serie_filter = Serie.objects.filter(slug=slug)
    serie_act = serie_filter.first()
    serie_id = serie_act.id
    cap_list = Caps.objects.filter(serie=serie_id)
    return render(request,"seriesapp/serie_list.html",{"cap_list":cap_list,"serie":serie_act})

def CapView (request,slug,no):
    serie_filter = Serie.objects.filter(slug=slug)
    serie_act = serie_filter.first()
    serie_id = serie_act.id
    cap=  Caps.objects.filter(no=no).filter(serie=serie_id).first()
    return render(request,"seriesapp/caps_detail.html",{"cap":cap,"serie":serie_act})

