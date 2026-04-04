from django.contrib import admin
from .models import Movie, Genre

# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'get_genres']
    filter_horizontal = ('genres',)

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = 'Genres'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']