# Generated by Django 4.1.4 on 2022-12-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0002_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
