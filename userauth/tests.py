from django.test import TestCase, Client
from django.urls import resolve
from django.contrib.auth.models import User
from django.contrib import auth
from .views import user_login

# Create your tests here.
class UserAuthTest(TestCase):
    '''
        URL Testcases
    '''
    def test_url_is_exist_login(self):
        response = Client().get('/userauth/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_cannot_access_login_if_user_already_authenticated(self):
        new_account = User.objects.create_user('dummy', '', 'password_for_dummy')
        new_account.set_password('password_for_dummy')
        new_account.save()

        c = Client()
        login = c.login(username = new_account.username, password = 'password_for_dummy')
        response = c.get('/userauth/login/')
        self.assertEqual(response.status_code, 302)

    def test_register(self) :
        response = self.client.post("/userauth/login/", data={'first_name' : 'kak', 'last_name' : 'pewe',  'username' : 'testing123123', 'password1' : 'testpassword123','password2' : 'testpassword123', 'Sign Up':"Sign Up"})
        self.assertEqual(response.status_code,302)
        self.assertEqual(1, User.objects.count())

    def test_url_logout(self) :
        response = Client().get("/userauth/logout")
        self.assertEqual(response.status_code,301)
        user = auth.get_user(self.client)
        self.assertEqual(False, user.is_authenticated)