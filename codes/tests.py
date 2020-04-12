import datetime

from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import classe

PASSWORD_INPUT = '<input name="password" type="password" placeholder="Mot de passe"/>'

# Create your tests here.
class classeTestCase(TestCase):
    def setUp(self):
        user=User.objects.create_user('user', password='Promo2023')
        user.save()
        self.client = Client()


    def test_code_views(self):
        """.    Views generate pages correctly"""
        c = classe.objects.create(nom="math", classe_groupe="3R", prof="M. Traore", commnence=datetime.datetime.now(tz=None), fini=datetime.datetime.now(tz=None), code=111111, link="google.com", posted=True)
        self.client.post('/login/', {'password': 'Promo2023'}, follow=True)
        response = self.client.get('/codes', follow=True)
        self.assertContains(response, "math")
        self.assertContains(response, "3R")
        self.assertContains(response, "M. Traore")
        self.assertContains(response, "111111")
    

    def test_login_fails(self):
        """.    Logging in with the wrong passwords fails"""
        response = self.client.post('/login/', {'password': 'not the password'}, follow=True)
        self.assertContains(response, "Mauvais mot de passe")


    def test_login_required(self):
        """.    All pages redirect to login if not authenticated"""
        response = self.client.get('/', follow=True)
        self.assertContains(response, PASSWORD_INPUT)

        response = self.client.get('/codes', follow=True)
        self.assertContains(response, PASSWORD_INPUT)

        response = self.client.get('/soumission', follow=True)
        self.assertContains(response, PASSWORD_INPUT)

    
    def test_login_works(self):
        """.    Logging in redirects to all classes"""
        response = self.client.post('/login/', {'password': 'Promo2023'}, follow=True)
        self.assertContains(response, "Matières")


    def test_urls_work(self):
        """.    All urls exists"""
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/codes', follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/soumission', follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/sdf', follow=True)
        self.assertEqual(response.status_code, 404)
    
    



"""
Running tests: `python3 -W ignore -m coverage run manage.py test  -v 2 `
Getting reports: `python3 -m coverage html --omit "/Users/tommcn/Library/Python/3.7/lib/python/site-packages/*","codes/migrations/*" `
"""
