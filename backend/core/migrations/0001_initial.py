# Generated by Django 5.1.3 on 2024-11-25 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AgriImplement",
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
                ("name", models.CharField(max_length=200)),
                (
                    "implement_type",
                    models.CharField(
                        choices=[
                            ("PLOUGH", "Plough"),
                            ("HARROW", "Harrow"),
                            ("SEEDER", "Seeder"),
                            ("SPRAYER", "Sprayer"),
                            ("OTHER", "Other"),
                        ],
                        max_length=20,
                    ),
                ),
                ("brand", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("EXCELLENT", "Excellent"),
                            ("GOOD", "Good"),
                            ("FAIR", "Fair"),
                            ("POOR", "Poor"),
                        ],
                        max_length=20,
                    ),
                ),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Conversation",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to="users.profile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to="users.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="core.conversation",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OperatorProfile",
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
                ("phone_number", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=200)),
                ("experience_years", models.IntegerField()),
                ("certifications", models.TextField(blank=True)),
                ("hourly_rate", models.DecimalField(decimal_places=2, max_digits=6)),
                ("is_verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TractorListing",
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
                ("brand", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
                ("year", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("EXCELLENT", "Excellent"),
                            ("GOOD", "Good"),
                            ("FAIR", "Fair"),
                            ("POOR", "Poor"),
                        ],
                        max_length=20,
                    ),
                ),
                ("horsepower", models.FloatField()),
                ("location", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("working_hours", models.IntegerField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.profile"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TractorImage",
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
                ("image", models.ImageField(upload_to="tractor_images/")),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "tractor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="core.tractorlisting",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="conversation",
            name="listing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.tractorlisting",
            ),
        ),
    ]
