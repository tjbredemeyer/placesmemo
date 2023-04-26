"""This is the views.py file for the places app"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from memos.models import Memo
from .models import Place
from .forms import PlaceForm


class PlacesListView(ListView):
    """This view returns a list of places."""

    model = Place
    template_name = "place_list.html"
    extra_context = {"page_title": "Browse Places"}

    def get_queryset(self):
        """This method returns a list of places for the current user."""
        place_list = Place.objects.all()
        return place_list


class PlaceDetailView(DetailView):
    """This view returns a single place."""

    model = Place
    template_name = "place_detail.html"
    context_object_name = "place"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        memos = Memo.objects.filter(place=self.object)
        context["memos"] = memos
        return context


class PlaceCreateView(LoginRequiredMixin, CreateView):
    """This view creates a place."""

    model = Place
    form_class = PlaceForm
    template_name = "place_form.html"
    extra_context = {"page_title": "Create a Place"}

    def form_valid(self, form):
        # Create an instance of the model, but don't save it yet
        place = form.save(commit=False)
        # Slugify the name and set it as the slug field
        place.slug = slugify(place.name)
        # Save the instance
        place.save()
        messages.success(self.request, "Place created successfully")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("places:detail", kwargs={"slug": self.object.slug})


class PlaceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view updates a place's name, rating, tags, or notes"""

    model = Place
    form_class = PlaceForm
    template_name = "place_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        place_name = self.object.name
        context["page_title"] = "Updating " + place_name
        return context

    def test_func(self):
        """Check if the current user owns the object."""
        obj = self.get_object()
        return obj.owner == self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Place updated successfully")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "Failed to update place")
        return response

    def get_success_url(self):
        return reverse_lazy("places:detail", kwargs={"slug": self.object.slug})


class PlaceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """This view deletes a place."""

    model = Place

    def test_func(self):
        """Check if the current user owns the object."""
        obj = self.get_object()
        return obj.owner == self.request.user

    def get(self, request, *args, **kwargs):
        # Call the delete method directly
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Place deleted successfully")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("places:list")
