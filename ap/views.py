from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Movie, Rating, Actors, Directors
from .serializers import MovieSerializer, RatingSerializer, UserSerializer, ActorsSerializer, DirectorsSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Movie.objects.all()
    

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Rating.objects.all()


class ActorsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Actors.objects.all()


class DirectorsViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Directors.objects.all()