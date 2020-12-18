from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('', views.report, name="report"),
    path('lihatReport/', views.lihat, name="lihat")
]