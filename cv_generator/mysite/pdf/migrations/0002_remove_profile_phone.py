# Generated by Django 3.1 on 2020-08-17 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]