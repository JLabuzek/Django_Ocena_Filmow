from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Movie, Rating, ActorsandDirectors
from .serializers import MovieSerializer, RatingSerializer, UserSerializer, ActorsAndDirectorsSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Movie.objects.all()

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Rating.objects.all()


class ActorsAndDirectorsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorsAndDirectorsSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = ActorsandDirectors.objects.all()