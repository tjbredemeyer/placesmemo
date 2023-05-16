"""Models for the Lists app"""
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
    """Define the list model"""

    name = models.CharField(max_length=255, null=False)
    slug = models.CharField(max_length=255, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        """Define the object display"""
        return str(self.name)

    def get_absolute_url(self):
        """Returns the url to access a particular list instance."""
        return reverse("memo_detail", args=[str(self.pk)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
