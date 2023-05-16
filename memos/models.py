"""The memos module"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from places.models import Place
from lists.models import List
from tags.models import Tag


# Create your models here.
class Memo(models.Model):
    """This class represents a memo."""

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)
    rating = models.IntegerField(blank=True)
    notes = models.TextField(blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=False)
    tags = models.ManyToManyField(Tag, blank=True)
    lists = models.ManyToManyField(List, blank=True)

    objects = models.Manager()

    def __str__(self):
        """Return the default output for Memo."""
        return f"{self.place} by {self.created_by}: rating: {self.rating}, pk: {self.pk}"

    def get_absolute_url(self):
        """Returns the url to access a particular memo instance."""
        return reverse("memos:detail", args=[str(self.pk)])
