import django_filters

from main.models import *
from django import forms

class DonaturFilter(forms.ModelForm):
    class Meta :
        model = Pendonor
        fields = [
            'name', "name"
        ]