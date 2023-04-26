"""URL configuration for accounts app."""
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.AccountView.as_view(), name="account"),
    path("edit/", views.AccountUpdateView.as_view(), name="edit_account"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
