from django.shortcuts import render  # for templates

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializer import MovieSerializer, MovieMiniSerializer
from .models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    # If we are just returning one specific movie then  return all the informations defined in MovieSerializer
    serializer_class = MovieSerializer

    # IF we are returning a list of all the objects to the users then we overide the list method in order to modify what
    # we are returning by adding the MovieMiniSerializer that return only (id, title)
    def list(self, request, *args, **kwargs):
        # Get our data
        movies = Movie.objects.all()
        # Decide how we want to return it to the API, the specific fields that we want to return defined in serializer
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
