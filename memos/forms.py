"""This module contains the forms for the places app."""
from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    """This form is used to create and update places."""

    tags = forms.CharField(widget=forms.Textarea(attrs={"rows": 1}))
    lists = forms.SelectMultiple()

    class Meta:
        """This class defines the fields that are used in the form."""

        model = Memo
        fields = ["place", "rating", "tags", "notes", "lists"]
