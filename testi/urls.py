from django.urls import path, include
from . import views
app_name = 'testi'

urlpatterns = [
    path('', views.tampilan, name='tampilan'),
    path('atur/', views.testi, name='testi'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
]
