from django.urls import path

from .views import update_image, user

app_name = "user"

urlpatterns = [
    path("", user, name="user"),
    path("update_image/", update_image, name="update_image"),
]
