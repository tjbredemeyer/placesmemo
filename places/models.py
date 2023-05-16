"""This module contains the models for the places app."""
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


class Place(models.Model):
    """This class represents a place."""

    name = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    location = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.TimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """Returns the url to access a particular place instance."""
        return reverse("place_detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        """Override the save method to auto generate the slug field"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
