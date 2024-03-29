# Generated by Django 4.1.3 on 2023-05-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_patient_patient_no_alter_patient_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="physiosession",
            name="physiosession_no",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="physiosessionadmission",
            name="patient_type",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="patient",
            name="patient_no",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
