# Generated by Django 4.1.4 on 2022-12-24 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0007_director_alter_movie_rating_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
