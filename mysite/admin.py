from django.contrib import admin
from mysite.models import MovieList, Movie

@admin.register(MovieList)
class MovieListAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'mlist', 'counter')