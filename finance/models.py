from django.db import models

# Create your models here.
class Citoyen (models.Model):
    cin = models.CharField(max_length=8, unique=True)
    amende = models.CharField(max_length=100)
    pinalité = models.CharField(max_length=100)