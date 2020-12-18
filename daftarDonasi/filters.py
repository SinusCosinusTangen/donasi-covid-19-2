import django_filters

from main.models import *

class DonaturFilter(django_filters.FilterSet):
    class Meta:
        model = Pendonor
        fields = '__all__'
        exclude = ['phone_number', 'amount', 'method', 'messages']