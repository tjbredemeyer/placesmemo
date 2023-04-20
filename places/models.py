'''This module contains the models for the places app.'''
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Place(models.Model):
    '''This class represents a place.'''
    name = models.CharField(max_length=255, blank=False)
    slug = models.SlugField(
        unique=True,
        max_length=255,
        null=True,
        blank=True,
        default=''
    )
    rating = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True)
    tags = TaggableManager(related_name='places', blank=True)
    yelp_id = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)


    def get_absolute_url(self):
        '''Returns the url to access a particular place instance.'''
        return reverse('place_detail', args=[str(self.slug)])
