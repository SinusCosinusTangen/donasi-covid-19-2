from django.shortcuts import render, HttpResponse, redirect
from .models import Question, Answer
from .form import AnswerForm
from django.contrib.auth.models import User



# Create your views here.


def pertanyaan(request) :
    questions = Question.objects.all()
    search = request.GET.get('search')

    if search : 
        questions = Question.objects.filter(question__icontains=search)

    context = {
        'questions' : questions
    }

    return render(request, 'pertanyaan/pertanyaan.html', context)

def detail(request, pk) :
    #print(form.user)
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
            #form = AnswerForm(initial={'user': request.user})
            
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