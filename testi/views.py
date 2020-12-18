from django.shortcuts import render, redirect
from .forms import Testimoni_Form
from .models import Testi

def tampilan(request):
    testi = Testi.objects.all()
    context = {
        'semua_testi':testi
    }
    return render(request, 'tampilanTesti.html', context)

def testi(request):
    testi_form = Testimoni_Form(request.POST or None)
    if request.method == "POST":
        if testi_form.is_valid():
            testi_form.save()

        return redirect('testi:tampilan')
    
    context = {
        'testi_form' : testi_form
    }
    return render(request, 'isiTesti.html', context)



