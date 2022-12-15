# Generated by Django 4.1.3 on 2022-12-12 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_ward_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physiosession',
            name='therapist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
