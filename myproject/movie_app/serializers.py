from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.fields import DateField
from .models import (
    Country, Director, Actor, Genre, Movie,
    MovieLanguages, Moments, Rating, UserProfile, Favorite, History
)
from rest_framework_simplejwt.tokens import RefreshToken

class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('__all__')

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('__all__')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name']



class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']

class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S')
    user = UserProfileRatingSerializer()
    class Meta:
        model = Rating
        fields = ['id', 'user', 'parent', 'stars', 'text', 'created_date']


class MovieListSerializer(serializers.ModelSerializer):
    year = DateField(format='%Y')
    country = CountrySerializer(many=True )
    genre = GenreSerializer(many=True)


    class Meta:
        model = Movie
        fields = ['id','movie_image','movie_name', 'year', 'country', 'genre','status_movie']

class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    genre = GenreSerializer(many=True)
    year = serializers.DateField(format='%d-%m-%Y')
    movie_frames = MomentsSerializer(many=True, read_only=True)
    movie_videos = MovieLanguagesSerializer(many=True, read_only=True)
    movie_ratings = RatingSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['movie_name','year', 'country', 'director', 'actor', 'genre', 'types',
                  'movie_time', 'movie_trailer', 'description', 'movie_image', 'status_movie','movie_frames', 'movie_videos','get_avg_rating','get_count_people','movie_ratings']
    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self,obj):
        return obj.get_count_people()

class CountryDetailSerializer(serializers.ModelSerializer):
    country_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'country_movies']

class DirectorDetailSerializer(serializers.ModelSerializer):
    age = DateField(format='%d-%m-%Y')
    director_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ['director_name','director_image', 'bio', 'age', 'director_movies']


class ActorDetailSerializer(serializers.ModelSerializer):
    actor_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['actor_name','actor_image','age','bio','actor_movies']


class GenreDetailSerializer(serializers.ModelSerializer):
    genre_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id','genre_name', 'genre_movies' ]
