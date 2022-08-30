from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    cumpleaños = models.DateField()
    edad = models.IntegerField()
