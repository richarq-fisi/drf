from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
