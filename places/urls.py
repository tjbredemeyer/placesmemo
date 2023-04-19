'''URLs for the places app.'''
from django.urls import path

from . import views

urlpatterns = [
    path(
        '', 
        views.PlacesListView.as_view(),
        name="places_list"
    ),
    path(
      'add/',
      views.PlaceCreateView.as_view(),
      name='place_add'
    ),
    # TODO not working
    path(
      '<int:pk>/edit/',
       views.PlaceUpdateView.as_view(),
      name='place_edit'
    ),
    # TODO not functional
    path(
        '<int:pk>/delete/', 
        views.PlaceDeleteView.as_view(),
        name='place_delete'
    ),
    # TODO not functional
    path(
        'add-tag/',
        views.add_tag,
        name='add_tag'
    ),
]
