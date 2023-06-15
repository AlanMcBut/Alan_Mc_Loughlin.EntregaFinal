from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(),
            "email": forms.TextInput(),
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput(),
        }
        help_texts = {k : "" for k in fields}