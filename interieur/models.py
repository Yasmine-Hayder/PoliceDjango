from django.db import models

# Create your models here.
class citoyen (models.Model):
    cin = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=20)
    etat= models.CharField(max_length=8)

