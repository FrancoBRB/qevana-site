# Generated by Django 3.2.6 on 2021-09-04 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.IntegerField(verbose_name='Año'),
        ),
    ]