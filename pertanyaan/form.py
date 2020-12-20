from django import forms

from .models import Answer, Question

class AnswerForm(forms.ModelForm):
    class Meta :
        model = Answer
        fields = [
            "answer"
        ]

class QuestionForm(forms.ModelForm):
    class Meta :
        model = Question
        fields = [
            "question"
        ]

    

    
