from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.conf import settings
from uuid import uuid4
from sorl.thumbnail import get_thumbnail

import os


class Profile(models.Model):
    """Класс профиля"""
    def upload_to(self, filename):
        email = self.user.email
        file_name, file_extension = os.path.splitext(filename)
        filename = f"{uuid4().hex}{file_extension}"
        return "images/{0}/{1}".format(email, filename)

    def user_email(self):
        return self.user.email

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        "фотография",
        upload_to=upload_to,
        null=True,
        blank=True,
    )

    def get_image_300x300(self):
        return get_thumbnail(
            self.image,
            "50x50",
            quality=100,
        )

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src='{self.get_image_300x300().url}' "
                f"width='50' "
                f"height='50'>"
            )
        return "Нет изображения"

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профиля"

        db_table = "profiles"

    def __str__(self):
        return f"{self.user}"

    def update(self):
        BASE_DIR = settings.BASE_DIR

        email = self.user_email()
        try:
            path_to_directory = os.path.join(
                BASE_DIR, "media", "images", email
            )
            for filename in os.listdir(path_to_directory):
                path_to_file = os.path.join(path_to_directory, filename)
                os.remove(path_to_file)
        except Exception as e:
            pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
