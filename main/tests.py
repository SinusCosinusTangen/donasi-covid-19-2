from django.test import LiveServerTestCase, TestCase, tag, Client
from django.urls import reverse, resolve
from selenium import webdriver
from .models import Pendonor
from pertanyaan.models import Question
from main import views


@tag('functional')
class FunctionalTestCase(LiveServerTestCase):
    """Base class for functional test cases with selenium."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Change to another webdriver if desired (and update CI accordingly).
        options = webdriver.chrome.options.Options()
        # These options are needed for CI with Chromium.
        options.headless = True  # Disable GUI.
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


class MainTestCase(TestCase):
    def test_root_url_status_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # You can also use path names instead of explicit paths.
        response = self.client.get(reverse('main:donate'))
        self.assertEqual(response.status_code, 200)



class MainFunctionalTestCase(FunctionalTestCase):
    def test_root_url_exists(self):
        self.selenium.get(f'{self.live_server_url}/')
        html = self.selenium.find_element_by_tag_name('html')
        self.assertNotIn('not found', html.text.lower())
        self.assertNotIn('error', html.text.lower())

class DonorTestCase(TestCase):
    def test_url (self) :
        response1  = Client().get("/donate/")
        self.assertEqual(response1.status_code,200)

    def test_template_used(self) :
        response = Client().get("/donate/")
        self.assertTemplateUsed(response, "main/donate.html")

    def test_str_equal_to_name(self):
        Pendonor.objects.create(name="Riris", phone_number="08117777774", amount="500000", method="Transfer Bank", messages="Semangat yah")
        obj = Pendonor.objects.get(pk=1)
        self.assertEqual(str(obj), obj.name)
    
    def test_donasi(self) :
        response = self.client.post('/donate/', data={"name":"Riris", "phone_number":"08117777774", "amount":"500000", "method":"Transfer Bank", "messages":"Semangat yah"})
        self.assertEqual(Pendonor.objects.count(), 1)

    def test_function_views_donate_used(self):
        function = resolve('/donate/')
        self.assertEqual(function.func, views.donate)
   
    def test_model_used_in_donate_html(self):
        Pendonor.objects.create(name="Riris", phone_number="08117777774", amount="500000", method="Transfer Bank", messages="Semangat yah")
        count_the_message = Pendonor.objects.all().count()
        self.assertEquals(count_the_message, 1)

    