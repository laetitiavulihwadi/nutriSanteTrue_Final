# Generated by Django 5.0.3 on 2024-04-01 10:14

import pages.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_useragent'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=pages.models.filepath),
        ),
    ]
