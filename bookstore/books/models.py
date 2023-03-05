from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    publisher = models.CharField(max_length=100)