# Generated by Django 4.1 on 2022-09-04 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('caught', models.BooleanField()),
            ],
        ),
    ]