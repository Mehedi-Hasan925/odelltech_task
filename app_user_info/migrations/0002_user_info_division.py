# Generated by Django 3.2.9 on 2021-11-21 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='Division',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
