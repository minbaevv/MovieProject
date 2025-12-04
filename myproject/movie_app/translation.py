from modeltranslation.translator import register, TranslationOptions
from .models import Country, Director, Actor, Genre, Movie, MovieLanguages


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('director_name', 'bio',)


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('actor_name', 'bio',)


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('genre_name',)


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description',)

@register(MovieLanguages)
class MovieLanguagesTranslationOptions(TranslationOptions):
    fields = ('language',)