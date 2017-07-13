from django.db import models
from django.contrib.auth.models import User


class Dog(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    def __str__(self):
    	return self.name
