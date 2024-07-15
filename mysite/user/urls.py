from django.urls import path

from .views import delete_booking, update_image, user

app_name = "user"

urlpatterns = [
    path("", user, name="user"),
    path("delete_booking/", delete_booking, name="delete_booking"),
    path("update_image/", update_image, name="update_image"),
]
