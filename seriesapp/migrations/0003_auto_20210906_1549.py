# Generated by Django 3.2.6 on 2021-09-06 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seriesapp', '0002_auto_20210906_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caps',
            name='title',
        ),
        migrations.RemoveField(
            model_name='seasons',
            name='title',
        ),
    ]
