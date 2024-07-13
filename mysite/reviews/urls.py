from django.urls import path
from .views import reviews

app_name = "reviews"

urlpatterns = [
    path("", reviews, name="reviews"),
]
