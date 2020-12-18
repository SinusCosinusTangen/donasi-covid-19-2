from django.urls import path
from . import views

app_name = 'daftarDonasi'

urlpatterns = [
    path('', views.daftarDonasi, name="daftarDonasi")
]