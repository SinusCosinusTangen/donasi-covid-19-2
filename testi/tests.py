from django.test import TestCase, Client
from django.urls import resolve
from .models import Testi
from .views import testi, tampilan, searchh
from django.urls import resolve, Resolver404
from .apps import TestiConfig
from django.contrib.auth.models import User

class TestRouting(TestCase):
    def test_event_url_is_exist(self):
        response = Client().get('/testi/')
        self.assertEqual(response.status_code, 200)
    def test_event2_url_is_exist(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
        
        self.client.login(username='testing', password='testing8888') # login user

        response = Client().get('/testi/atur/')
        self.assertEqual(response.status_code, 302)

        self.client.logout()
        self.assertEqual(response.status_code, 302)
    def test_event3_url_is_exist(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
        
        self.client.login(username='testing', password='testing8888') # login user

        response = Client().get('/testi/searchh')
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        self.assertEqual(response.status_code, 200)
    def test_event_using_template(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
        
        self.client.login(username='testing', password='testing8888') # login user

        response = Client().get('/testi/')
        self.assertContains(response, "What Do")

        self.client.logout()
        response = Client().get('/testi/')
        self.assertEqual(response.status_code, 200)
       
        self.assertTemplateUsed(response, 'tampilanTesti.html')
    def test_event2_using_template(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
      
        self.client.login(username='testing', password='testing8888') # login user

        response = Client().get('/testi/atur/')
        self.assertEqual(response.status_code, 302)

        self.client.logout()
        response = Client().get('/userauth/login/')
        self.assertTemplateUsed(response, 'userauth/userauth.html')

    def test_event3_using_template(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
        
        self.client.login(username='testing', password='testing8888') # login user

        response = Client().get('/testi/searchh')
        self.assertContains(response, "search testimonee")

        self.client.logout()
        response = Client().get('/userauth/login/')
        self.assertTemplateUsed(response, 'userauth/userauth.html')

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
    def test_delete(self):
        user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
      
        self.client.login(username='testing', password='testing8888') # login user

        testiku = Testi.objects.create(nama="Lary", institusi="Bikiny bottom", testimoni="Tuan Krabs peelit")
        testiku.delete()
        self.assertEqual(Testi.objects.all().count(), 0)
    def test_view_is_using_function_render(self):
        try:
            user = User.objects.create_user('testing', 'testing@testing.com', 'testing8888') # create user
        
            self.client.login(username='testing', password='testing8888') # login user
            found = resolve('/testi/searchh/')
            self.assertEqual(found.func, searchh)
        except Resolver404:
            pass



class TestApp(TestCase):
    def test_app(self):
        self.assertEqual(TestiConfig.name, "testi")





