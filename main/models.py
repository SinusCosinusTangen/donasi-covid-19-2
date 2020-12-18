from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField

# Create your models here.
class Pendonor(models.Model):
    METHOD = (
        ('Transfer Bank', 'Transfer Bank'),
        ('Pepew Pay', 'Pepew Pay'),
        ('Go Pew', 'Go Pew'),
        ('OPEW', 'OPEW'),
        ('Pew Aja', 'Pew Aja')
    )
    name = models.CharField(max_length = 100, null = True)
    phone_number = models.CharField(max_length = 100, null = True)
    amount = models.CharField(max_length = 100, null = True)
    method = models.CharField(max_length = 100, null = True, choices = METHOD)
    messages = models.CharField(max_length = 500, null = True)

    def __str__(self):
        return self.name