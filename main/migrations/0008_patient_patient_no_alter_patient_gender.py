# Generated by Django 4.1.3 on 2023-05-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_physiosession_admission_no_physiosession_more_notes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="patient_no",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="patient",
            name="gender",
            field=models.CharField(max_length=10),
        ),
    ]
