from django import forms
from movieapp.models import Genres

genre_list = Genres.objects.all()
GENRE_CHOICES = ()

for genre in genre_list:
    GENRE_CHOICES += (
        (str(genre), str(genre)),
    )

TYPE_CHOICES = (
    ('1','Serie'),
    ('2','Película'),
)


class AdvancedSearchForm(forms.Form):  
    Tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'bg-dark text-light m-2'}),choices=TYPE_CHOICES,required=True)
    Año = forms.IntegerField(min_value=1950,max_value=2021,required=True,widget=forms.NumberInput(attrs={ 'class':'bg-dark text-light m-2'}))
    Genero = forms.ChoiceField(widget=forms.Select(attrs={'class': 'bg-dark text-light m-2'}),choices=GENRE_CHOICES,required=True)

    
 