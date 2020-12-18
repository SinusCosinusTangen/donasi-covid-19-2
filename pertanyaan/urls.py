from django.urls import path

from . import views

app_name = 'pertanyaan'

urlpatterns = [
    path('', views.pertanyaan, name='pertanyaan'),
    path('<str:pk>/', views.detail, name='detail'),
]
