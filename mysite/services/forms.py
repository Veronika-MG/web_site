from django import forms
from django.utils import timezone

from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["datetime"]
        widgets = {
            "datetime": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ДД-ММ-ГГГГ ЧЧ:ММ",
                },
                format="%d-%m-%Y %H:%M",
            ),
        }
