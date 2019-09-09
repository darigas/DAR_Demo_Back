from rest_framework import serializers
from kino_kz.models import Movie, ComingSoonMovie, Cinema, City


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ComingSoonMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComingSoonMovie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

