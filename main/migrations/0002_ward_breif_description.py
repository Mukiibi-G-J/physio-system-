# Generated by Django 4.1.3 on 2022-12-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ward',
            name='breif_description',
            field=models.TextField(blank=True, default='No description', null=True),
        ),
    ]
