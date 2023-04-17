'''This module contains the views for the API'''
from rest_framework import viewsets
from places.models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    '''This class represents the viewset for the Place model.'''
    queryset = Place.objects.all().order_by('name')
    serializer_class = PlaceSerializer
