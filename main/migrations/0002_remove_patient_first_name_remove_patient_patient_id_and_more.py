# Generated by Django 4.1.3 on 2023-05-15 10:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="patient_id",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="pin_no",
        ),
        migrations.RemoveField(
            model_name="patient",
            name="surname",
        ),
    ]