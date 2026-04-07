from django.db import models

# Create your models here.

def movie_directory_path(instance, filename):
# Crea el path de la imagen del la pelicula correspondiente

    return "movies/MEDIA_ROOT/{0}/{1}".format(instance.title, filename)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    genres = models.ManyToManyField('movies.Genre', related_name='movies')
    cover = models.ImageField(upload_to=movie_directory_path)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        import traceback
        print("SE ESTA GUARDANDO UNA PELICULA")
        traceback.print_stack()
        super().save(*args, **kwargs)
    
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name