"""This is the views for lists app"""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
from .models import List
from .forms import ListForm


class UserListsView(LoginRequiredMixin, ListView):
    """This is the view that returns all the lists created by a user"""

    # TODO userlistview
    # TODO lists.html
    model = List
    context_object_name = "list_list"
    template_name = "lists.html"
    extra_context = {"page_title": "Browse lists"}

    def get_queryset(self):
        """This method returns a list of places for the current user."""
        return List.objects.filter(created_by=self.request.user)


class ListDetailView(LoginRequiredMixin, DetailView):
    """This is the listed view of the memos within a single list."""

    model = List
    context_object_name = "list"
    template_name = "list_detail.html"

    def get_queryset(self):
        """This method returns a list of places for the current user."""
        return List.objects.filter(created_by=self.request.user)

    def get_context_data(self, queryset=None, **kwargs):
        obj = super().get_object(queryset=queryset)
        context = super().get_context_data(**kwargs)
        context["list_slug"] = obj.slug
        context["page_title"] = "Browse memos in " + obj.name
        context["tags"] = (
            Memo.objects.filter(created_by=self.request.user, lists=obj.pk)
            .values_list("tags__name", flat=True)
            .distinct()
        )
        context["memos"] = (
            Memo.objects.all()
            .filter(created_by=self.request.user, lists=obj.pk)
            .order_by("-rating")
        )
        return context


class ListCreateView(LoginRequiredMixin, CreateView):
    """This is the create a list view"""

    model = List
    form_class = ListForm
    template_name = "list_form.html"
    extra_context = {"page_title": "Create a list"}

    def form_valid(self, form):
        # Create an instance of the model, but don't save it yet
        list_obj = form.save(commit=False)
        # Slugify the name and set it as the slug field
        list_obj.created_by = self.request.user
        list_obj.slug = slugify(list_obj.name)
        # Save the instance
        list_obj.save()
        messages.success(self.request, "List created successfully")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("lists:detail", kwargs={"slug": self.object.slug})


class ListUpdateView(UpdateView):
    """This is the list update view"""

    # TODO listupdateview
    model = List
    form_class = ListForm
    template_name = "list_form.html"

    def get_context_data(self, queryset=None, **kwargs):
        obj = super().get_object(queryset=queryset)
        context = super().get_context_data(**kwargs)
        context["list_name"] = obj.name
        context["page_title"] = "Update list: " + obj.name
        return context

    def form_valid(self, form):
        # Create an instance of the model, but don't save it yet
        list_obj = form.save(commit=False)
        # Slugify the name and set it as the slug field
        list_obj.created_by = self.request.user
        list_obj.slug = slugify(list_obj.name)
        # Save the instance
        list_obj.save()
        messages.success(self.request, "List created successfully")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("lists:detail", kwargs={"slug": self.object.slug})


class ListDeleteView(DeleteView):
    """This is the list delete view"""

    # TODO listdeleteview
    model = List

    def test_func(self):
        """Check if the current user owns the object."""
        obj = self.get_object()
        return obj.created_by == self.request.user

    def get(self, request, *args, **kwargs):
        # Call the delete method directly
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Memo deleted successfully")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("lists:list")
