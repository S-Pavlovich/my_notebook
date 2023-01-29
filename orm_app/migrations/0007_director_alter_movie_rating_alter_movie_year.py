# Generated by Django 4.1.4 on 2022-12-24 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0006_alter_movie_viewed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1888), django.core.validators.MaxValueValidator(2100)]),
        ),
    ]
