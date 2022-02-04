from asyncio.format_helpers import _format_callback_source
from multiprocessing import context
from pyexpat import model
from re import template
import re
from sre_constants import SUCCESS
from xml.dom.expatbuilder import theDOMImplementation
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import changeDpForm, editprofileForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView 
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonial,
		Certificate
	)

from django.views import generic


from . forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		testimonials = Testimonial.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		return context


class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


def RegisterView(request):
	template_name = "main/register.html"
	if(request.method=='POST'):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		
		if(password1==password2):
			if User.objects.filter(username=username).exists():
				messages.error(request,"Username Taken. Please enter another Username")
				return render(request,'main/register.html')
			elif User.objects.filter(email=email).exists():
				messages.error(request,"This email has already been registered. Use another email")
				return render(request,'main/register.html')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
				user.save()
				messages.success(request, 'Registration Successful.')
				return redirect('/')

		else:
			messages.error(request,"Passwords do not match.")
			return render(request,'main/register.html')
	else: return render(request,'main/register.html')

def login(request):
	template_name="main/login.html"
	if request.method == 'GET':
		return render(request,'main/login.html')

	else:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect("/")
		else:
			messages.error(request,"Invalid Credentials")
			return render(request,'main/login.html')
		

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-detail.html"

def profileView(request):
	template_name="main/profile.html"
	return render(request,"main/profile.html")

def logout(request):
	
	auth.logout(request)
	return redirect("/")




class ChangeDP(generic.UpdateView):
	form_class = changeDpForm
	template_name = "main/updateImage.html"
	success_url = "/"

	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = "/"

class editprofileView(generic.UpdateView):
	form_class = editprofileForm
	template_name = "main/editprofile.html"
	success_url = "/"

	def get_object(self):
		return self.request.user





class dpChangeView(generic.UpdateView):
	template_name = "main/updateImage.html"
	form_class = changeDpForm
	success_url = "/"
	
	def get_object(self):
		return self.request.user


def editDPView(request):
	user = request.user
	if request.method=='POST':
			newImage = request.FILES['avatar']
			obj = UserProfile.objects.get(user=user)
			obj.avatar = newImage
			obj.save()
			return render(request,'main/profile.html')
	else:
		return render(request, 'main/updateImage.html')

def SetUserImageDefault(self):
	self.user.userprofile.avatar.delete(save=True)
	print(self.user.first_name)
	return render(self,"main/profile.html")

def donate(request):
	user = request.user
	if request.method=='POST':
		amount = request.POST['donation']
		obj= UserProfile.objects.get(user=user)
		
		obj.donation = (int(0 if obj.donation is None else obj.donation) + int(amount))
		obj.save()
		print(obj.donation)
		return render(request,"main/profile.html")
	else:
		return render(request,"main/donate.html")