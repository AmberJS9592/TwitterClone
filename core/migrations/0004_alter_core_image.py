# Generated by Django 4.1 on 2022-08-25 05:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_like_core_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='Image'),
        ),
    ]