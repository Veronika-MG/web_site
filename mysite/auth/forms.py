from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

from mysite.mixins import BaseFormMixin


class UserRegisterForm(BaseFormMixin, UserCreationForm):
    """Класс, отвечающий за форму регистрации"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_field_attributes()

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class MyLoginForm(auth.forms.AuthenticationForm, BaseFormMixin):
    """Класс, отвечающий за форму авторизация"""
    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.set_field_attributes()
