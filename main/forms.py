from django import forms
from .models import Pendonor

class FormPendonor(forms.ModelForm):
    class Meta :
        model = Pendonor
        fields = [
            'name',
            'phone_number',
            'amount',
            'method',
            'messages'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'method': forms.Select(attrs={'class': 'form-control'}),
            'messages': forms.Textarea(attrs={'class': 'form-control'})
        }