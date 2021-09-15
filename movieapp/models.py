from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField


class Genres(models.Model):
    genre_name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    title= models.CharField('Título',max_length=150,unique=True)
    alt_title = models.CharField('Título en Ingles',max_length=150)
    slug = models.SlugField('Slug (título entre guiones)',unique=True)
    country = models.CharField('País',max_length=56)
    date = models.IntegerField('Año')
    synopsis= models.TextField('Sinopsis')
    genres= models.ManyToManyField(Genres,verbose_name='Generos')
    thumbnail= models.CharField('Miniatura (225x125)',max_length=300)
    portrait= models.CharField('Portada (300x450)',max_length=300)
    url= models.CharField('URL Opción 1:',max_length=300)
    url2= models.CharField('URL Opción 2:',max_length=300,blank=True)
    url3= models.CharField('URL Opción SubEng:',max_length=300,blank=True)
    recommended = models.BooleanField('Recomendada?',default=False)
    premiere = models.BooleanField('Estreno?',default=False)
    up_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['up_date']


