"""This is the Tags model."""
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Tag(models.Model):
    """This is the Tag object. Tags will be associated with Memos."""

    name = models.CharField(max_length=255, blank=False, null=False)
    slug = models.CharField(max_length=255, blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        """Return the string version of the Tags object."""
        return str(self.name)

    def get_absolute_url(self):
        """Returns the url to access a particular Tag instance."""
        return reverse("place_detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
