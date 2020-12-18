from django import forms

from pertanyaan.models import Question

class QuestionForm(forms.ModelForm):
    class Meta :
        model = Question
        fields = [
            'name', "question"
        ]

    
