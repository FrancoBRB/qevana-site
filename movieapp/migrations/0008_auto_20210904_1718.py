# Generated by Django 3.2.6 on 2021-09-04 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_movie_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Slug (título entre guines)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='portrait',
            field=models.ImageField(upload_to='', verbose_name='Portada (300x450)'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.CharField(max_length=200, verbose_name='URL Embed'),
        ),
    ]