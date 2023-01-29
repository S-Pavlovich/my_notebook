from django.contrib import admin
from .models import Movie, Director, Actor
from django.db.models import QuerySet


# Register your models here.
admin.site.register(Director)
admin.site.register(Actor)


class RatingFilter(admin.SimpleListFilter):
    title = 'Rating filter'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('0-50', 'Low'),
            ('50-70', 'Middle'),
            ('70-100', 'High')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '0-50':
            return queryset.filter(rating__lte=50)
        elif self.value() == '70-100':
            return queryset.filter(rating__gte=70)
        elif self.value() == '50-70':
            return queryset.filter(rating__lt=70).filter(rating__gt=50)
        else:
            return queryset.filter()


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['name', 'year', 'director', 'rating', 'rating_status', 'viewed']
    list_editable = ['year', 'director', 'rating', 'viewed']
    filter_horizontal = ['actors']
    ordering = ['name']
    list_per_page = 20
    actions = ['set_viewed']
    search_fields = ['name']
    list_filter = ['year', RatingFilter, 'viewed']

    @admin.display(ordering='rating', description='State')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Not recommend'
        elif mov.rating < 70:
            return 'Not yet'
        else:
            return 'Highly recommend'

    @admin.action(description='Change view status ')
    def set_viewed(self, request, qs: QuerySet):
        count_updated = qs.update(viewed=Movie.Yes)
        self.message_user(
            request,
            f'Have been updated {count_updated} movies.'
        )
