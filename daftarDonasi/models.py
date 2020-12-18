from django.db import models

from main.models import Pendonor
# Create your models here.
class DaftarPendonor(models.Model):
    pendonor = models.ForeignKey(Pendonor, on_delete=models.PROTECT)