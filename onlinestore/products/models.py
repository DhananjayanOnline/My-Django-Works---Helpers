from enum import unique
from django.db import models

# Create your models here.

class Mobiles(models.Model):
    name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    specs = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    band = models.CharField(max_length=100)

    def __str__(self):
        return self.name
