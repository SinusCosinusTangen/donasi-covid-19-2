from django.shortcuts import render, redirect
from .forms import Testimoni_Form
from .models import Testi
from django.contrib.auth.models import User

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import TestiSerializer

def tampilan(request):
    testi = Testi.objects.all()
    context = {
        'semua_testi':testi
    }
    return render(request, 'tampilanTesti.html', context)

def testi(request):
    if request.user.is_authenticated:
        testi_form = Testimoni_Form(request.POST or None)
        if request.method == "POST":
            if testi_form.is_valid():
                testi_form.save()

            return redirect('testi:tampilan')
        
        context = {
            'testi_form' : testi_form
        }
        return render(request, 'isiTesti.html', context)
    else:
        return redirect('userauth:login')

def delete(request, delete_id):
    Testi.objects.filter(id = delete_id).delete()
    return redirect('testi:tampilan')

def searchh(request):
    testi = Testi.objects.all()
    context = {
        'semua_testi':testi
    }
    return render(request, 'testimonee.html', context)
 


@csrf_exempt
def name_list(request) :
    try :
        arguments = request.GET['q']
    except :
        arguments = ""

    if request.method == "GET" :
        institusi = Testi.objects.filter(institusi__icontains=arguments)
        serializer = TestiSerializer(institusi, many=True)
        return JsonResponse(serializer.data, safe=False)





 