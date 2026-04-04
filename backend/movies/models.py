from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    genres = models.ManyToManyField('movies.Genre', related_name='movies')
    
    def __str__(self):
        return self.title
    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name