"""This module contains the forms for the places app."""
from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    """This form is used to create and update places."""

    # TODO reconfigure PlaceForm
    class Meta:
        """This class defines the fields that are used in the form."""

        model = Place
        fields = ["name", "location"]
