from django import forms

from mysite.mixins import BaseFormMixin
from .models import Profile


class ProfileImageForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
