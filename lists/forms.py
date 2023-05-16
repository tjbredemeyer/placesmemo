"""This module contains the forms for the places app."""
from django import forms
from .models import List


class ListForm(forms.ModelForm):
    """This form is used to create and update places."""

    class Meta:
        """This class defines the fields that are used in the form."""

        model = List
        fields = ["name"]
