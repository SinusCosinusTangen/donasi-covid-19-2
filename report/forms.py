from django.forms import ModelForm
from .models import Report

class reportIssue(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'