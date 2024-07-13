from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_email",
        "image_tmb",
    )
    list_display_links = ("id", "image_tmb")
