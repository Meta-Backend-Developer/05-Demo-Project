# Generated by Django 4.1.5 on 2023-01-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0003_rename_name_person_person_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="age",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
