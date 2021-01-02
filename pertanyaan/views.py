from django.shortcuts import render, HttpResponse, redirect
from .models import Question, Answer
from .form import AnswerForm, QuestionForm
from django.contrib.auth.models import User

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import QuestionSerializer



# Create your views here.


def pertanyaan(request) :
    questions = Question.objects.all()
    search = request.GET.get('search')
    
    

    if request.method == "POST" :
        if request.POST["addQuestion"] == "add" :
            if request.user.is_authenticated :
                return redirect("pertanyaan:add")
            else :
                return redirect("userauth:login")

    if search :
        questions = Question.objects.filter(question__icontains=search)

    

    context = {
        'questions' : questions
    }

    return render(request, 'pertanyaan/pertanyaan.html', context)


def detail(request, pk) :
    form = AnswerForm()
    context= { 
        'form' : form,
        'mauTanya' : False 
    }
    try:
        Question.objects.get(id=pk)
        context['question'] = Question.objects.get(id=pk)
    except:
        context['question'] = ""

    if request.method == 'POST' :
        if request.user.is_authenticated:
            
            if request.POST.get("addAnswer") == "mauTanya" :
                context['mauTanya'] = True
            if request.POST.get("addAnswer") == "add": 
                form = AnswerForm(request.POST)
                if form.is_valid() :
                    ans = form.save(commit=False)
                    ans.user = request.user 
                    ans.save()
                    Question.objects.get(pk = pk).answer.add(ans)
                    return redirect("pertanyaan:detail", pk)
        else :
            return redirect("userauth:login")



    return render(request, 'pertanyaan/detail.html', context)



def add(request) :
    form = QuestionForm()
    context = {'form' : form}
    if request.user.is_authenticated :
        if request.method == "POST" :
            form = QuestionForm(request.POST)
            if form.is_valid() :
                form = form.save(commit=False)
                form.user = request.user 
                form.save()
                return redirect('pertanyaan:pertanyaan')

        return render(request, 'pertanyaan/add.html', context)
    else :
        return redirect("userauth:login")


@csrf_exempt
def question_list(request) :
    try :
        arugment = request.GET['q']
    except :
        arugment = ""

    if request.method == "GET" :
        question = Question.objects.filter(question__icontains=arugment)
        serializer = QuestionSerializer(question, many=True)
        return JsonResponse(serializer.data, safe=False)