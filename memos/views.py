"""This is the views.py file for the places app"""
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from places.models import Place
from tags.models import Tag
from lists.models import List
from tags.views import clear_empty_tags
from .models import Memo
from .forms import MemoForm


class MemosListView(LoginRequiredMixin, ListView):
    """This view returns a list of places."""

    model = Memo
    context_object_name = "memo_list"
    template_name = "memo_list.html"
    extra_context = {"page_title": "Browse Memos"}

    def get_queryset(self):
        """This method returns a list of places for the current user."""
        return Memo.objects.filter(created_by=self.request.user).order_by(
            "-rating"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = (
            Memo.objects.filter(created_by=self.request.user)
            .values_list("tags__name", flat=True)
            .distinct()
        )
        return context


class MemoDetailView(LoginRequiredMixin, DetailView):
    """This view returns a single place."""

    model = Memo
    template_name = "memo_detail.html"
    context_object_name = "memo"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        """This method returns the context for the view."""
        context = super().get_context_data(**kwargs)
        memo = context.get("memo")
        context["page_title"] = "Memo for " + memo.place.name
        return context

    def get_object(self, queryset=None):
        """Return the object if it belongs to the current user."""
        obj = super().get_object(queryset=queryset)
        if obj.created_by != self.request.user:
            raise Http404()
        return obj


class MemoCreateView(LoginRequiredMixin, CreateView):
    """This view updates a place's name, rating, tags, or notes"""

    model = Memo
    form_class = MemoForm
    template_name = "memo_form.html"

    def get_context_data(self, **kwargs):
        """This method returns the context for the view."""
        context = super().get_context_data(**kwargs)
        place_id = self.request.GET.get("place_id")
        place_name = Place.objects.get(id=place_id).name
        users_lists = List.objects.all().filter(created_by=self.request.user)
        context["page_title"] = "Add a new memo for " + place_name
        context["place_id"] = place_id
        context["place_name"] = place_name
        print(users_lists)
        context["lists"] = users_lists
        return context

    def add_list(self, memo, lists):
        """This function adds tags to a memo."""
        for list_name in lists:
            list_obj = List.objects.get_or_create(name=list_name)
            memo.lists.add(list_obj[0].id)
        return memo

    def add_tag(self, memo, tags):
        """This function adds tags to a memo."""
        tag_names = [tag.strip().lower() for tag in tags.split(",")]
        for tag_name in tag_names:
            tag = Tag.objects.get_or_create(name=tag_name)
            memo.tags.add(tag[0].id)
        return memo

    def create_memo(self, data, user):
        """This function creates a memo from the data in the form"""
        place = data.get("place")
        rating = data.get("rating")
        notes = data.get("notes")
        tags = data.get("tags")
        lists = data.get("lists")
        memo = Memo.objects.create(
            place=place,
            rating=rating,
            notes=notes,
            created_by=user,
        )
        if tags:
            self.add_tag(memo, tags)
        if lists:
            self.add_list(memo, lists)
        memo.save()
        return memo

    def form_valid(self, form):
        user = self.request.user
        memo = self.create_memo(form.cleaned_data, user)
        messages.success(self.request, "Memo created successfully")
        return redirect("memos:detail", pk=memo.pk)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "Memo could not be created")
        return super().form_invalid(form)


class MemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view updates a place's name, rating, tags, or notes"""

    model = Memo
    form_class = MemoForm
    template_name = "memo_form.html"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        memo = self.model.objects.get(id=self.kwargs["pk"])
        users_lists = List.objects.all().filter(created_by=self.request.user)
        context["page_title"] = f"Update memo for {memo.place.name}"
        context["place_id"] = memo.place.id
        context["place_name"] = memo.place.name
        print(users_lists)
        context["lists"] = users_lists
        return context

    def test_func(self):
        """Check if the current user owns the object."""
        obj = self.get_object()
        return obj.created_by == self.request.user

    def add_list(self, memo, lists):
        """This function adds tags to a memo."""
        for list_name in lists:
            list_obj = List.objects.get_or_create(name=list_name)
            memo.lists.add(list_obj[0].id)
        return memo

    def add_tag(self, memo, tags):
        """This function adds tags to a memo."""
        tag_names = [tag.strip().lower() for tag in tags.split(",")]
        for tag_name in tag_names:
            tag = Tag.objects.get_or_create(name=tag_name)
            memo.tags.add(tag[0].id)
        clear_empty_tags()
        return memo

    def update_memo(self, data, memo):
        """This function creates a memo from the data in the form"""
        memo.tags.clear()
        memo.lists.clear()
        memo.place = data.get("place")
        memo.rating = data.get("rating")
        memo.notes = data.get("notes")
        lists = data.get("lists")
        tags = data.get("tags")
        if tags:
            self.add_tag(memo, tags)
        if lists:
            self.add_list(memo, lists)
        memo.save()
        return memo

    def form_valid(self, form):
        memo = Memo.objects.get(id=self.kwargs["pk"])
        self.update_memo(form.cleaned_data, memo)
        messages.success(self.request, "Memo created successfully")
        return redirect("memos:detail", pk=memo.pk)

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        messages.error(self.request, "Failed to update place")
        return response

    def get_success_url(self):
        return reverse_lazy("memos:detail", kwargs={"pk": self.object.pk})


class MemoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """This view deletes a place."""

    model = Memo
    pk_url_kwarg = "pk"

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
        return reverse_lazy("memos:list")
