"""URLs for the tags app."""
from django.urls import path
from . import views

# set the namespace for the app
app_name = "tags"

urlpatterns = [
    path("<slug:slug>/", views.TagListView.as_view(), name="list"),
]
