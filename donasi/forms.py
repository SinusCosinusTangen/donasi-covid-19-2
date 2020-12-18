from django import forms
from .models import Donasi

class FormLembaga(forms.ModelForm):
    class Meta :
        model = Donasi
        fields = '__all__'

        widgets = {
            'lembaga' : forms.TextInput(attrs={'placeholder':'Name'}),
            'description' : forms.Textarea(attrs={'placeholder':'Description'}),
        }