from django import forms
from .models import Testi
# Create your views here.

class Testimoni_Form(forms.ModelForm):
    class Meta:
        model = Testi
        fields = [
            'nama',
            'institusi',
            'testimoni'
        ]
        widgets = {
            'nama': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Name'
				}
			),
            'institusi': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Institution'
				}
			),
            'testimoni': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Testimonial',
                    'height':400 
				}
			)
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

