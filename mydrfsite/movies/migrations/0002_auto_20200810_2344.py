# Generated by Django 3.1 on 2020-08-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='ratind',
            new_name='rating',
        ),
    ]
