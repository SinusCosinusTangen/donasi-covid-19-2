from donasi.views import seeInstitution
from django.urls import path
from . import views

app_name = 'donasi'

urlpatterns = [
    path('', views.institutionReg, name="institution"),
    path('seeInstitution/', views.seeInstitution, name="seeInstitution"),
]