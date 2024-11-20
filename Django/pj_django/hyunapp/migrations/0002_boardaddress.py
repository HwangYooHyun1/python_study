# Generated by Django 5.1.3 on 2024-11-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hyunapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardAddress",
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
                ("writer", models.CharField(max_length=200)),
                ("email", models.TextField()),
                ("subject", models.TextField()),
                ("content", models.TextField()),
                ("rdate", models.DateTimeField()),
            ],
        ),
    ]