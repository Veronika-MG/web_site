# Generated by Django 4.2.11 on 2024-07-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=64, verbose_name="заголовок")),
                (
                    "text",
                    models.TextField(default="отсутствует", verbose_name="описание"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="цена"
                    ),
                ),
            ],
            options={
                "verbose_name": "услуга",
                "verbose_name_plural": "услуги",
                "db_table": "services",
            },
        ),
    ]