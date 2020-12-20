from django.urls import path

from . import views

app_name = 'pertanyaan'

urlpatterns = [
    path('', views.pertanyaan, name='pertanyaan'),
    path('<int:pk>/', views.detail, name='detail'),
    path("add/", views.add, name="add" ),
]
