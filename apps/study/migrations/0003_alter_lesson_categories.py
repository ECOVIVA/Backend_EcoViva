# Generated by Django 5.1.7 on 2025-03-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_achievement_achievementrule_userachievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='study.category'),
        ),
    ]
