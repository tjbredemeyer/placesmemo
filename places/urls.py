'''URLs for the places app.'''
from django.urls import path

from . import views

urlpatterns = [
    path(
        '', 
        views.PlacesListView.as_view(),
        name="places"
    ),
    path(
        'create/',
        views.PlaceCreateView.as_view(),
        name='place_create'
    ),
    path(
        '<slug:slug>/',
        views.PlaceDetailView.as_view(),
        name='place_detail'
    ),
    path(
        '<slug:slug>/update/',
        views.PlaceUpdateView.as_view(),
        name='place_update'
    ),
    path(
        '<slug:slug>/delete/',
        views.PlaceDeleteView.as_view(),
        name='place_delete'
    ),
]
