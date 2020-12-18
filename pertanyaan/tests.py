from django.test import TestCase, Client
from .models import Question, Answer

# Create your tests here.

class MainTestCase(TestCase) :
    def test_url (self) :
        response2  = Client().get("/question/")
        self.assertEqual(response2.status_code,200)

        response3  = Client().get("/question/1/")
        self.assertEqual(response3.status_code,200)

    def test_model (self) :
        ans = Answer.objects.create(name='rafi', answer='ini jawabannya')
        Question.objects.create(name='rafi2', question='ini pertanyaan')
        Question.objects.get(pk=1).answer.add(ans)

        self.assertEqual(1, Question.objects.count())
        self.assertEqual(1, Answer.objects.count())

    def test_template_used(self) :
        response = Client().get("/question/")
        self.assertTemplateUsed(response, "pertanyaan/pertanyaan.html")

        response2 = Client().get("/question/1/")
        self.assertTemplateUsed(response2,"pertanyaan/detail.html")
    
    def test_element_in_template(self) :
        ans = Answer.objects.create(name='rafi', answer='ini jawabannya')
        Question.objects.create(name='rafi2', question='ini pertanyaan')
        Question.objects.get(pk=1).answer.add(ans)

        response = Client().get("/question/")
        html_response = response.content.decode('utf8')
        self.assertIn("ini pertanyaan", html_response)


        response = Client().get("/question/1/")
        html_response = response.content.decode('utf8')
        self.assertIn("ini jawabannya", html_response)

    def test_search(self) :
        Question.objects.create(name='rafi2', question='ini pertanyaan')
        response = self.client.get('/question/', data={'search' : "ini"})
        html_response = response.content.decode('utf8')
        self.assertIn("ini", html_response)

        response = self.client.get('/question/', data={'search' : "itu"})
        html_response = response.content.decode('utf8')
        self.assertIn("There are no question", html_response)

    def test_menjawab(self) :
        Question.objects.create(name='rafi2', question='ini pertanyaan')
        response = self.client.post('/question/1/', data={'name' : 'Rafi', "answer" : "ini pertanyaan", "addAnswer" : "mauTanya", "addAnswer" : "add" })
        self.assertEqual(Question.objects.get(pk=1).answer.all()[0].answer, "ini pertanyaan")
        


