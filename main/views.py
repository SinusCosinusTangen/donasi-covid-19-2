from django.shortcuts import render, redirect
from .forms import FormPendonor
from .models import Pendonor
from .form import QuestionForm
from django.contrib import messages

def donate(request):
    form = FormPendonor(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'main/donate.html', context)


def home(request):
    form = QuestionForm()

    if request.method == "POST" :
        if request.POST.get("ask") :
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("pertanyaan:pertanyaan")
        if request.POST.get("seeAll") :
            return redirect("pertanyaan:pertanyaan")
    context = {
        'form' : form
    }
    return render(request, 'main/home.html', context)
