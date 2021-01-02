from rest_framework import serializers
from .models import Testi

class TestiSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Testi
        fields = ['nama', 'institusi']
