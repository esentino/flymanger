# Generated by Django 5.1 on 2024-08-18 16:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_plaincargo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserWerehouse',
            new_name='UserWarehouse',
        ),
    ]
