from django.urls import path
from .views import services, detail, booking

app_name = "services"

urlpatterns = [
    path("", services, name="services"),
    path("detail/<int:id>/", detail, name="detail"),
    path("booking/<int:id>/", booking, name="booking"),
]
