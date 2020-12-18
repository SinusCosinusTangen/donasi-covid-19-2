from daftarDonasi.filters import DonaturFilter
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.models import *

# Create your views here.
def daftarDonasi(request):
    pendonor = Pendonor.objects.all()
    page = request.GET.get('page', 1)
    myFilter = DonaturFilter(request.GET, queryset=pendonor)
    donatur = myFilter.qs
    paginator = Paginator(donatur, 10)

    try:
        donatur = paginator.page(page)
    except PageNotAnInteger:
        donatur = paginator.page(1)
    except EmptyPage:
        donatur = paginator.page(paginator.num_pages)

    context = {'donatur':donatur, 'myFilter':myFilter}
    return render(request, 'daftarDonasi/daftarDonasi.html', context)