from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet, ActorsandDirectorsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('actors-and-directors', ActorsandDirectorsViewSet)

urlpatterns = [
    path('', include(router.urls))
]