# Generated by Django 4.2.11 on 2024-03-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='num_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
