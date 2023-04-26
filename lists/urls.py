"""URLs for the lists app."""
from django.urls import path

from . import views

# set the namespace for the app
app_name = "lists"

urlpatterns = [
    # view available lists created by the user
    path(
        "",
        views.UserListsView.as_view(),
        name="list",
    ),
    # create a new list
    path(
        "create/",
        views.ListCreateView.as_view(),
        name="create",
    ),
    # view the memos in a specific list
    path(
        "<slug:slug>/",
        views.ListDetailView.as_view(),
        name="detail",
    ),
    # update list name and bulk remove memos from list
    path(
        "<slug:slug>/update/",
        views.ListUpdateView.as_view(),
        name="update",
    ),
    # delete list
    path(
        "<slug:slug>/delete/",
        views.ListDeleteView.as_view(),
        name="delete",
    ),
]
