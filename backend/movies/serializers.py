from rest_framework import serializers
from .models import Movie, Genre

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    duration = serializers.DurationField()
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    def create(self, data):
        genres = data.pop('genres')
        movie = Movie.objects.create(**data)
        movie.genres.set(genres)
        return movie
    
    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.duration = data.get('duration', instance.duration)

        if 'genres' in data:
            instance.genres.set(data['genres'])

        instance.save()
        return instance