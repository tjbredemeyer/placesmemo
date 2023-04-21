'''This is the views.py file for the places app'''
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Place
from .forms import PlaceForm


class PlacesListView(LoginRequiredMixin, ListView):
    '''This view returns a list of places.'''
    model = Place
    context_object_name = 'places_list'
    template_name = 'places.html'

    def get_queryset(self):
        '''This method returns a list of places for the current user.'''
        return Place.objects.filter(created_by=self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Place.objects.filter(
            created_by=self.request.user
        ).values_list(
            'tags__name',
            flat=True
        ).distinct()
        return context


class PlaceDetailView(LoginRequiredMixin, DetailView):
    '''This view returns a single place.'''
    model = Place
    template_name = 'place_detail.html'
    context_object_name = 'place'
    pk_url_kwarg = 'place_id'


    def get_object(self, queryset=None):
        '''Return the object if it belongs to the current user.'''
        obj = super().get_object(queryset=queryset)
        if obj.created_by != self.request.user:
            raise Http404()
        return obj


class PlaceCreateView(LoginRequiredMixin, CreateView):
    '''This view updates a place's name, rating, tags, or notes'''
    model = Place
    form_class = PlaceForm
    template_name = 'place_form.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add new place'  # set the title to 'Create'
        return context


    def form_valid(self, form):
        # Create an instance of the model, but don't save it yet
        place = form.save(commit=False)

        # Set the user to the current logged-in user
        place.created_by = self.request.user

        # Slugify the name and set it as the slug field
        place.slug = slugify(place.name)

        # Save the instance
        place.save()

        messages.success(self.request, 'Place created successfully')

        return super().form_valid(form)


class PlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''This view updates a place's name, rating, tags, or notes'''
    model = Place
    form_class = PlaceForm
    template_name = 'place_form.html'
    pk_url_kwarg = 'place_id'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'  # set the title to 'Update'
        return context


    def test_func(self):
        '''Check if the current user owns the object.'''
        obj = self.get_object()
        return obj.created_by == self.request.user


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Place updated successfully')
        return response


    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Failed to update place')
        return response


    def get_success_url(self):
        return reverse_lazy('place_detail', kwargs={'slug': self.object.slug})


class PlaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''This view deletes a place.'''
    model = Place
    pk_url_kwarg = 'place_id'

    def test_func(self):
        '''Check if the current user owns the object.'''
        obj = self.get_object()
        return obj.created_by == self.request.user

    def get(self, request, *args, **kwargs):
        # Call the delete method directly
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Place deleted successfully')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('places')
