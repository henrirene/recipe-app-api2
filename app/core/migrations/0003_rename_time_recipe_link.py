# Generated by Django 3.2.15 on 2022-08-12 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='link',
        ),
    ]
