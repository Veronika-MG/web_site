from django.urls import path
from .views import homepage

app_name = "homepage"

urlpatterns = [
    path("", homepage, name="homepage"),
]
