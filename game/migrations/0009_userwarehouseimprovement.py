# Generated by Django 5.1 on 2024-08-18 19:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_rename_plaincargo_planecargo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWarehouseImprovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invest_money', models.IntegerField(default=0)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.cargo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('cargo', 'user')},
            },
        ),
    ]
