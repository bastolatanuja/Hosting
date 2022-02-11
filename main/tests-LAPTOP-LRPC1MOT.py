from audioop import reverse
from http import client
from unicodedata import name
from urllib import response
from django.test import SimpleTestCase, TestCase,Client
from main.views import IndexView
from . import views
from django.urls import reverse,resolve
from django.contrib.auth.models import User,auth
import json
from .models import (
ContactProfile,
Skill,
UserProfile,
Blog,
Portfolio,
Testimonial,
Certificate,
Media,
)



#url tests
class TestUrls(SimpleTestCase):

def test_resolve_to_Homepage(self):
url = reverse("main:home")
resolver = resolve(url)
self.assertEquals(resolver.func.__name__,views.IndexView.as_view().__name__)



def test_resolve_to_create_portfolio(self):
url = reverse("main:addPortfolio")
resolver = resolve(url)
self.assertEquals(resolver.func.__name__,views.addPortfolio.as_view().__name__)

def test_resolve_to_update_portfolio(self):
url = reverse("main:updatePortfolio",args=[1])
resolver = resolve(url)
self.assertEquals(resolver.func.__name__,views.updatePortfolio.as_view().__name__)



def test_resolve_to_delete_PortfolioDetail(self):
url = reverse("main:deletePortfolio",args=[1])
resolver = resolve(url)
self.assertEquals(resolver.func.__name__,views.deletePortfolioView.as_view().__name__)



#views tests



class TestViews(TestCase):



def test_homepage_view(self):
client = Client()
response = client.get(reverse("main:home"))
self.assertEquals(response.status_code,200)
self.assertTemplateUsed(response,'main/index.html')

def test_blogpage_view(self):
client = Client()
response = client.get(reverse("main:blogs"))
self.assertEquals(response.status_code,200)
self.assertTemplateUsed(response,'main/blog.html')



def test_login_view(self):
user = User.objects.create_user(username="testcatse", password="1234567", email="random@gmail.com",first_name="Test",last_name="Case")
user.save()
client = Client()
logged_in = client.login(username = 'testcase',password ='1234567')
url = reverse('main:login')
response = client.get(url)
self.assertEquals(response.status_code,200)
self.assertTemplateUsed(response,'main/login.html')

def test_create_skill_view(self):
client = Client()
user = auth.authenticate(username='tanuja',password='xxxabc123')
url = reverse('main:addSkill')
response = client.post(url,{
'name' : 'testSkill',
'score':90,
})
self.assertEquals(response.status_code,302)
self.assertRedirects(response,'/allskills/')

def test_delete_skill_view(self):
client = Client()
user = auth.authenticate(username='tanuja',password='xxxabc123')
newSkill = Skill.objects.create(name = 'testSkill', score = 90)
url = reverse('main:deleteSkill',args=[newSkill.id])
response=client.delete(url)
self.assertEquals(response.status_code,302)
self.assertRedirects(response,'/allskills/')