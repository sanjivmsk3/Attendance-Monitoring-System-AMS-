# Generated by Django 3.1 on 2021-10-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clockinout_total_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clockinout',
            name='total_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
