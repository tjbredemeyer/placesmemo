'''This module contains the models for the places app.'''
from django.db import models
from taggit.managers import TaggableManager


class Place(models.Model):
    '''This class represents a place.'''
    name = models.CharField(max_length=60, unique=True)
    rating = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    tags = TaggableManager()
    yelp_id = models.CharField(max_length=60, null=True, blank=True)
    location = models.CharField(max_length=250, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)
