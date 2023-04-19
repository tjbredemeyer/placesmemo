'''This is the views.py file for the places app'''
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Place
from .forms import PlaceForm


def add_tag(request):
    '''This view adds a tag to a place.'''
    pass


class PlacesListView(ListView):
    '''This view returns a list of places.'''
    model = Place
    context_object_name = 'place_list'
    template_name = 'places_list.html'

    def get_queryset(self):
        '''This method returns a list of places.'''
        places = list(Place.objects.all())
        return places

    def get(self, request, *args, **kwargs):
        '''This method returns a list of places.'''
        places = Place.objects.all()
        return render(
            request,
            'places_list.html', 
            {
                'places': places, 
                'range': range(5)
            }
        )

class PlaceCreateView(CreateView):
    '''This view allows a user to create a new place.'''
    model = Place
    form_class = PlaceForm
    success_url = reverse_lazy('places_list')


class PlaceUpdateView(UpdateView):
    '''This view allows a user to update a place.'''
    model = Place
    form_class = PlaceForm
    success_url = reverse_lazy('places_list')


class PlaceDeleteView(DeleteView):
    '''This view allows a user to delete a place.'''
    model = Place
    template_name = 'place_confirm_delete.html'
    success_url = reverse_lazy('place_list')
