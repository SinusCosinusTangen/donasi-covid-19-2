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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'method': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Method'}),
            'messages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Messages'})
        }