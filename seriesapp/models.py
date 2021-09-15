from django.db import models
from movieapp.models import Genres


class Serie(models.Model):
    title= models.CharField('Título',max_length=150,unique=True)
    season = models.IntegerField('Temporada')
    alt_title = models.CharField('Título en Ingles',max_length=150)
    slug = models.SlugField('Slug (título entre guiones)',unique=True)       
    country = models.CharField('País',max_length=56)
    date = models.IntegerField('Año')
    synopsis= models.TextField('Sinopsis')
    genres= models.ManyToManyField(Genres,verbose_name='Generos')
    thumbnail= models.CharField('Miniatura (225x125)',max_length=300)
    portrait= models.CharField('Portada (300x450)',max_length=300)
    recommended = models.BooleanField('Recomendada?',default=False) 
    up_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + str(self.season)

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
        ordering = ['up_date']



class Caps(models.Model):
    no = models.IntegerField('Episodio Numero')
    url= models.CharField('URL Opción 1:',max_length=300)
    url2= models.CharField('URL Opción 2:',max_length=300,blank=True)
    url3= models.CharField('URL Opción SubEng:',max_length=300,blank=True)   
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    def __str__(self):
        return "Episodio " + str(self.no) + " de " +  self.serie.title + " " + str(self.serie.season)

    class Meta:
        verbose_name = 'Capítulo'
        verbose_name_plural = 'Capítulos'
        ordering = ['no']
