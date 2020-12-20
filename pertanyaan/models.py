from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Answer(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(max_length=400)

    def __str__(self) :
        return self.answer

class Question(models.Model) :
    name = models.CharField(max_length=50)
    question = models.TextField(max_length=400)
    detail = models.TextField(max_length=400, blank=True, null=True)
    answer = models.ManyToManyField(Answer, blank=True)
    
    def __str__(self) :
        return self.question


