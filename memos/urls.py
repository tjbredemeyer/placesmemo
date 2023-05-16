"""URLs for the places app."""
from django.urls import path

from . import views

# set the namespace for the app
app_name = "memos"

urlpatterns = [
    # Memos list
    path(
        "",
        views.MemosListView.as_view(),
        name="list",
    ),
    # Create memo
    path(
        "create/",
        views.MemoCreateView.as_view(),
        name="create",
    ),
    # Memo detail
    path(
        "<int:pk>/",
        views.MemoDetailView.as_view(),
        name="detail",
    ),
    # Update memo
    path(
        "<int:pk>/update/",
        views.MemoUpdateView.as_view(),
        name="update",
    ),
    # Delete memo
    path(
        "<int:pk>/delete/",
        views.MemoDeleteView.as_view(),
        name="delete",
    ),
]
