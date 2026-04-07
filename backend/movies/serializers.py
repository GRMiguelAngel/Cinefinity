from rest_framework import serializers
from .models import Movie, Genre

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'duration', 'cover', 'genres']

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        return movie
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.duration = validated_data.get('duration', instance.duration)

        if 'genres' in validated_data:
            instance.genres.set(validated_data['genres'])

        instance.save()
        return instance