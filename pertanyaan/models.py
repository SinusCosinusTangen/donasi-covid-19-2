from django.db import models

# Create your models here.

class Answer(models.Model) :
    name = models.CharField(max_length=50)
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


