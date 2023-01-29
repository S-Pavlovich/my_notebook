from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=60)
    pages = models.IntegerField()
    year = models.IntegerField()


class Director(models.Model):
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Men'),
        (FEMALE, 'Woman'),
    ]
    name = models.CharField(max_length=60)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Actor {self.name}'
        else:
            return f'Actress {self.name}'


class Movie(models.Model):
    No = 'No'
    Yes = 'Yes'
    BEEN_VIEWED_CHOICES = [
        (No, 'No'),
        (Yes, 'Yes'),
    ]
    name = models.CharField(max_length=60)
    rating = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1),
                                                                    MaxValueValidator(100)])
    year = models.IntegerField(validators=[MinValueValidator(1888),
                                           MaxValueValidator(2100)])
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    viewed = models.CharField(max_length=3, choices=BEEN_VIEWED_CHOICES, default=No)
    slug = models.SlugField(default='', null=False, db_index=True)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.name}({self.year})'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

# from orm_app.models import Movie
