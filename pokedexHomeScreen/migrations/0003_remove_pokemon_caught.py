# Generated by Django 4.1 on 2022-09-05 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedexHomeScreen', '0002_rename_captured_pokemon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='caught',
        ),
    ]
