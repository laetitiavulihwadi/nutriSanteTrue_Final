# Generated by Django 5.0.4 on 2024-05-28 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_alter_recette_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='description',
            field=models.TextField(),
        ),
    ]