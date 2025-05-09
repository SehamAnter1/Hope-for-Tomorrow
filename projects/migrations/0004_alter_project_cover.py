# Generated by Django 5.1.4 on 2025-05-01 21:19

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projectimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='project_covers/'),
        ),
    ]
