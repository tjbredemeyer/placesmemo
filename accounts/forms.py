"""This module contains the forms used in the accounts app."""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """This form is used to register a new user."""

    class Meta:
        """This class defines the fields that are used in the form."""

        model = User
        fields = ["username", "email", "password1", "password2"]


class AccountUpdateForm(UserRegistrationForm):
    """This is the form to update user accounts."""

    # TODO create the account update form
    # TODO account_update.html
    # TODO account.html
    # TODO verify email
    # TODO reset password
