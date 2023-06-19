# Generated by Django 4.1.3 on 2023-05-19 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0013_physiosession_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="physiosession",
            name="admission_no",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="physio_admission_no",
                to="main.physiosessionadmission",
            ),
        ),
        migrations.AlterField(
            model_name="physiosession",
            name="physiosession_no",
            field=models.CharField(max_length=255),
        ),
    ]