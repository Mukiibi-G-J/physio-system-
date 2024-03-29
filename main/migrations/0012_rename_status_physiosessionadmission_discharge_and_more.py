# Generated by Django 4.1.3 on 2023-05-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_receipt_visit_no"),
    ]

    operations = [
        migrations.RenameField(
            model_name="physiosessionadmission",
            old_name="status",
            new_name="discharge",
        ),
        migrations.AlterField(
            model_name="physiosessionadmission",
            name="diagnosis",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="diagnosis_physio_admission",
                to="main.diagnosis",
            ),
        ),
        migrations.AlterField(
            model_name="physiosessionadmission",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="patient_physio_admission",
                to="main.patient",
            ),
        ),
    ]
