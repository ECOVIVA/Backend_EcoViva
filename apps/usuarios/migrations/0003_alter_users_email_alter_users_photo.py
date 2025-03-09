# Generated by Django 5.1.7 on 2025-03-08 23:49

import django.core.validators
import utils.image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_users_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), utils.image.validate_image_size, utils.image.validate_image_dimensions]),
        ),
    ]
