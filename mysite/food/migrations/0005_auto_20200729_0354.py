# Generated by Django 3.0.5 on 2020-07-29 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20200729_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcscupzLxCQNFwQUGXkiFWY9nQETaCbfaD8gHVIOxA7UI-Rkc&s', max_length=500, upload_to=''),
        ),
    ]
