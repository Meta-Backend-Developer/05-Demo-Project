# Generated by Django 4.1.5 on 2023-01-24 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
            ],
        ),
    ]
