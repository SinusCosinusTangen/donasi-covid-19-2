from django.shortcuts import render, redirect
from .forms import FormPendonor
from .models import Pendonor
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

    return render(request, 'main/home.html',)
