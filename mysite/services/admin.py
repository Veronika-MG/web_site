from django.contrib import admin
from .models import Service, Booking

admin.site.register(Service)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "service",
        "user",
        "datetime",
    )
