from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Review
        fields = ["text"]
