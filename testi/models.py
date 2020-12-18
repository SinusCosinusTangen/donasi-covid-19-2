from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Testi(models.Model):
    nama = models.CharField(max_length = 100)
    institusi=models.CharField(max_length=100)
    testimoni = models.TextField(max_length = 1000)
    tanggal_testi = models.DateField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['institusi','nama']),
            models.Index(fields=['nama'], name='nama_idx'),
        ]
    def __str__(self):
        return self.nama
