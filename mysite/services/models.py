from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    """Класс услуг"""
    title = models.CharField(
        verbose_name="заголовок",
        null=False,
        validators=[],
        max_length=64
    )
    text = models.TextField(
        verbose_name="описание",
        default="отсутствует",
    )
    price = models.DecimalField(
        verbose_name="цена",
        max_digits=10,
        decimal_places=2,
    )

    class Meta:
        verbose_name = "услуга"
        verbose_name_plural = "услуги"

        db_table = "services"

    def __str__(self):
        return f"{self.title} is {self.text}"


class Booking(models.Model):
    """Класс брони"""
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    datetime = models.DateTimeField(
        "Дата и время записи",
    )

    class Meta:
        verbose_name = "бронь"
        verbose_name_plural = "брони"

        db_table = "bookings"

    def __str__(self):
        return (
            f"Запись {self.user} на {self.datetime.strftime('%d-%m-%Y %H:%M')}"
        )
