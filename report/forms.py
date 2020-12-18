from django import forms
from .models import Report

class reportIssue(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder':'Name'}),
            'description' : forms.Textarea(attrs={'placeholder':'Description'}),
        }