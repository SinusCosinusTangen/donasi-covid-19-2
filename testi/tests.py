from django.test import TestCase, Client
from django.urls import resolve
from .models import Testi
from .views import testi, tampilan
from .apps import TestiConfig

class TestRouting(TestCase):
    def test_event_url_is_exist(self):
        response = Client().get('/testi/')
        self.assertEqual(response.status_code, 200)
    def test_event2_url_is_exist(self):
        response = Client().get('/testi/atur/')
        self.assertEqual(response.status_code, 200)
    
    def test_event_using_template(self):
        response = Client().get('/testi/')
        self.assertTemplateUsed(response, 'tampilanTesti.html')
    def test_event2_using_template(self):
        response = Client().get('/testi/atur/')
        self.assertTemplateUsed(response, 'isiTesti.html')


class TestModels(TestCase):
    def test_model_can_create(self):
        new_activity = Testi.objects.create(nama="Lary", institusi="Bikiny bottom", testimoni="Tuan Krabs peelit")
        counting_all_available_todo = Testi.objects.all().count()
        self.assertEqual(counting_all_available_todo, 1)

    def test_model_can_print(self):
        kegiatan = Testi.objects.create(nama="Lary", institusi="Bikiny bottom", testimoni="Tuan Krabs peelit")
        self.assertEqual(kegiatan.__str__(), "Lary")

class TestFunc(TestCase):
    def test_views1_func(self):
        found = resolve('/testi/')
        self.assertEqual(found.func, tampilan)
    def test_event_func(self):
        found = resolve('/testi/atur/')
        self.assertEqual(found.func, testi)

class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(TestiConfig.name, "testi")





