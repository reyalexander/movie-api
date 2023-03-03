from .models import Rent
from django.contrib.auth.models import User
from rest_framework import serializers
from user.serializer import UserSerializer
from movie.models import Movie
from movie.serializer import MovieSerializer


class RentSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    class Meta:
        model = Rent
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('request').method in ['GET']:
            user = UserSerializer(instance.user).data
            movie = MovieSerializer(instance.movie).data
            representation['user'] = user
            representation['movie'] = movie
        return representation
