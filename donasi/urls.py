from donasi.views import seeInstitution
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'donasi'

urlpatterns = [
    path('', views.institutionReg, name="institution"),
    path('seeInstitution/', views.seeInstitution, name="seeInstitution"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)