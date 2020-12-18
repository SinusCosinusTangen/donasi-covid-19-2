from django.test import TestCase, Client
from django.core.files.images import ImageFile
from django.test import LiveServerTestCase, TestCase, tag
from django.urls import reverse
from selenium import webdriver

from .models import Donasi

# Create your tests here.
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

class institutionTest(TestCase):

    def test_eksistensi_url(self):
        response = Client().get('/institution/')
        self.assertEquals(response.status_code, 200)

    def test_eksistensi_template(self):
        response = Client().get('/institution/')
        self.assertTemplateUsed(response, 'donasi/donasi.html')

    def test_eksistensi_judul_dan_tombol(self):
        response = Client().get('/institution/')
        html_response = response.content.decode('utf8')
        self.assertIn("Register Your Institution", html_response)
        self.assertIn("Submit", html_response)
        self.assertIn("See Institutions", html_response)

    def test_eksistensi_model(self):
        Donasi.objects.create(lembaga="Jaya berkah", description="Jaya berkah merupakan...")
        self.assertEquals(Donasi.objects.all().count(), 1)

    def test_eksistensi_lihat_institusi(self):
        response = Client().get('/institution/seeInstitution/')
        self.assertEquals(response.status_code, 200)
        
    def test_eksistensi_template_lihat_institusi(self):
        response = Client().get('/institution/seeInstitution/')
        self.assertTemplateUsed(response, 'donasi/lihat.html')

class MainFunctionalTestCase(FunctionalTestCase):
    def test_root_url_exists(self):
        self.selenium.get(f'{self.live_server_url}/')
        html = self.selenium.find_element_by_tag_name('html')
        self.assertNotIn('not found', html.text.lower())
        self.assertNotIn('error', html.text.lower())