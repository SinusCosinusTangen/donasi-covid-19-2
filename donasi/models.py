from django.db import models

# Create your models here.
class Donasi(models.Model):
    lembaga = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to="img")