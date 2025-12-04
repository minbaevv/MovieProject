from rest_framework import routers
from .views import (
    UserProfileViewSet, CountryListAPIView, CountryDetailAPIView, DirectorListAPIView, DirectorDetailAPIView,
    ActorListAPIView, ActorDetailSerializer,
    GenreListAPIView,GenreDetailAPIView, MovieListAPIView, MovieDetailAPIView, MovieLanguagesViewSet,
    MomentsViewSet, RatingViewSet, FavoriteViewSet, FavoriteMovieViewSet, HistoryViewSet, ActorDetailAPIView,RegisterView,LoginView,LogoutView
)
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'movie-languages', MovieLanguagesViewSet)
router.register(r'moments', MomentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-movies', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]