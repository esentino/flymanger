# Generated by Django 5.1 on 2024-08-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_cargoimprovement_income_bonus_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlainCargo',
            new_name='PlaneCargo',
        ),
    ]
