'''This module contains the forms for the places app.'''
from django import forms
from .models import Place

class PlaceForm(forms.ModelForm):
    '''This form is used to create and update places.'''
    class Meta:
        '''This class defines the fields that are used in the form.'''
        model = Place
        fields = ['name', 'rating', 'location', 'notes', 'tags', 'yelp_id']

    def clean_tags(self):
        '''This method returns a list of lowercase tags.'''
        tags = self.cleaned_data['tags']
        lowercase_tags = [tag.lower() for tag in tags]
        return lowercase_tags