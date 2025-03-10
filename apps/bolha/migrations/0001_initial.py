# Generated by Django 5.1.7 on 2025-03-07 19:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bubble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.users')),
            ],
            options={
                'verbose_name': 'Bubble',
                'verbose_name_plural': 'Bubbles',
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=256)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bubble', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bolha.bubble')),
            ],
            options={
                'verbose_name': 'Check-In',
                'verbose_name_plural': 'Check-Ins',
            },
        ),
    ]
