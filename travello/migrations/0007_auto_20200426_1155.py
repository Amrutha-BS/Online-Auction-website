# Generated by Django 3.0.2 on 2020-04-26 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0006_destination_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='phone',
        ),
    ]