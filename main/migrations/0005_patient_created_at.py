# Generated by Django 4.1.3 on 2022-12-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_physiosession_therapist'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
