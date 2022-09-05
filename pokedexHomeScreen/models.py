from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=10)
    image = models.CharField(max_length=100)

"""
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
"""