from donasi.forms import FormLembaga
from django.shortcuts import render, redirect
from .models import Donasi

# Create your views here.
def institutionReg(request):
    if request.user.is_authenticated:
        form = FormLembaga()
        context = {'form':form}
        if request.method == "POST": 
            form = FormLembaga(request.POST, request.FILES)
            if form.is_valid(): 
                form.save()
                text = "Institusi berhasil ditambahkan"
                context = {'text':text}
                # return render(request, "donasi/lihat.html", context)
                return redirect("donasi:institution")
    else :
        return redirect("userauth:login")

    return render(request, 'donasi/donasi.html', context)

def seeInstitution(request):
    institution = Donasi.objects.all()
    context = {'institution':institution}

    return render(request, 'donasi/lihat.html', context)