from datetime import datetime

from django.db import models

from user.models import Profile


class Review(models.Model):
    """Класс отзыва"""
    def user_email(self):
        return self.profile.user.email

    text = models.TextField(
        verbose_name="описание",
        default="",
    )
    profile = models.OneToOneField(
        Profile,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    date = models.DateField(
        verbose_name="дата написания", default=datetime.now
    )

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

        db_table = "reviews"

    def __str__(self):
        return f"{self.text}"
