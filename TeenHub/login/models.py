from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    user_number = models.IntegerField(unique=True, blank=False)
    name = models.CharField(max_length=200, blank=False)
    username = models.CharField(max_length=200, blank=False)
    dob = models.DateField(blank=False)
    age = models.IntegerField(blank=False)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
