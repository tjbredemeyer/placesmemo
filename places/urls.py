"""URLs for the places app."""
from django.urls import path

from . import views

# set the namespace for the app
app_name = "places"

urlpatterns = [
    # Places list
    path(
        "",
        views.PlacesListView.as_view(),
        name="list",
    ),
    # Create place
    path(
        "create/",
        views.PlaceCreateView.as_view(),
        name="create",
    ),
    # Place detail
    path(
        "<slug:slug>/",
        views.PlaceDetailView.as_view(),
        name="detail",
    ),
    # Update place
    path(
        "<slug:slug>/update/",
        views.PlaceUpdateView.as_view(),
        name="update",
    ),
    # Delete place
    path(
        "<slug:slug>/delete/",
        views.PlaceDeleteView.as_view(),
        name="delete",
    ),
]
