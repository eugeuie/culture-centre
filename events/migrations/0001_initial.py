# Generated by Django 4.1.1 on 2022-09-11 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("name", models.CharField(max_length=100)),
                ("activity", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Человек",
                "verbose_name_plural": "Люди",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                ("name", models.CharField(max_length=100)),
                ("building", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "verbose_name": "Место",
                "verbose_name_plural": "Места",
                "ordering": ["building"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("title", models.CharField(max_length=100)),
                (
                    "place",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="events.place",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("time", models.DateTimeField()),
                ("participants", models.ManyToManyField(to="events.person")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "События",
                "ordering": ["time"],
            },
        ),
    ]
