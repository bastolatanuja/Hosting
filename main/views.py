from asyncio.format_helpers import _format_callback_source
from dataclasses import field
from decimal import Clamped
from msilib.schema import ListView, Media
from multiprocessing import context
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from statistics import mode
from urllib import request
from xml.dom.expatbuilder import theDOMImplementation
from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import blogForm, certificateForm, changeDpForm, editprofileForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail 

#import pagination things
from django.core.paginator import Paginator
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
		name = self.request.POST.get('name')
		email = self.request.POST.get('email')
		message = self.request.POST.get('message')
		
		send_mail(
			'Message From' + name,
			message,
			email,
			['tanujabastola143@gmail.com',],
			fail_silently=False,
		)

		form.save()
		messages.success(self.request, 'Thank you.We received your message. We will be in touch soon.')
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
	user = self.user
	#self.user.userprofile.avatar.delete(save=True)
	return render(self,"main/deleteUserdp.html",{'user':user})

def delDp(request):
	if request.method=='POST':
		request.user.userprofile.avatar.delete(save=True)
		return render(request,"main/profile.html")
	else:
		return render(request,"main/deleteUserdp.html")



def admin(request):
	
	return render(request,"main/adminpanel.html")




def allportfolio(request):
	portfolios = Portfolio.objects.all()
	return render(request,"main/allportfolios.html",{'portfolios':portfolios})

def allcertificate(request):
	certificates = Certificate.objects.all()
	return render(request,"main/allcertificates.html",{'certificates':certificates})

def allcontactprofile(request):
	contactprofiles = ContactProfile.objects.all()
	return render(request,"main/allcontactprofile.html",{'contactprofiles':contactprofiles})









class testView(generic.ListView):
	model = Certificate
	template_name = "main/allcertificates.html"
	paginate_by =2



class addCertificateView(generic.CreateView):
	model = Certificate
	template_name = "main/addCertificate.html"
	fields = '__all__'


class allBlogsView(generic.ListView):
	model = Blog
	template_name = "main/allblogs.html"
	paginate_by = 2

class addBlogView(generic.CreateView):
	model = Blog
	template_name = "main/addBlog.html"
	fields = ('author','name','description','body','image','is_active')

class allContactProfiles(generic.ListView):
	model = ContactProfile
	template_name = "main/allContactProfiles.html"
	paginate_by =2
	
	
	
class contactDetailView(generic.DetailView):
	model = ContactProfile
	template_name = "main/contactDetails.html" 
	fields = '__all__'

class allMedias(generic.ListView):
	model = Media
	template_name = "main/allmedia.html"
	paginate_by = 1
	
	

class allPortfolioView(generic.ListView):
	model = Portfolio
	template_name = "main/allportfolios.html"
	paginate_by =2

class allSkill(generic.ListView):
	model = Skill
	template_name = "main/allskill.html"
	paginate_by = 2
	ordering=['id']

class allTestimonial(generic.ListView):
	model = Testimonial
	template_name = "main/alltestimonial.html"
	paginate_by =2

class allUserProfiles(generic.ListView):
	model = UserProfile
	template_name = "main/alluserprofile.html"

class addMediaView(generic.CreateView):
	model = Media
	template_name = "main/addMedia.html"
	fields = '__all__'

class addPortfolio(generic.CreateView):
	model = Portfolio
	template_name = "main/addPortfolio.html"
	fields = ('date','name','description','body','image','is_active')

class addSkill(generic.CreateView):
	model = Skill
	template_name = "main/addskill.html"
	fields = '__all__'

class addTestimonial(generic.CreateView):
	model = Testimonial
	template_name = "main/addTestimonial.html"
	fields = '__all__'

class updateBlogView(generic.UpdateView):
	model = Blog
	template_name = "main/editBlog.html"
	fields = ['author','name','description','body','image','is_active']

class updateCertificateView(generic.UpdateView):
	model = Certificate
	template_name = "main/editCertificate.html"
	fields = '__all__'

class updateMedia(generic.UpdateView):
	model = Media
	template_name = "main/editMedia.html"
	fields = '__all__'

class updatePortfolio(generic.UpdateView):
	model = Portfolio
	template_name = "main/editPortfolio.html"
	fields = ('date','name','description','body','image','is_active')

class updateSkill(generic.UpdateView):
	model = Skill
	template_name = "main/editSkill.html"
	fields = '__all__'

class updateTestimonial(generic.UpdateView):
	model = Testimonial
	template_name = "main/editTestimonial.html"
	fields = '__all__'

class updateUserProfile(generic.UpdateView):
	model = UserProfile
	template_name = "main/editUserProfile.html"
	fields = '__all__'

class deleteBlogView(generic.DeleteView):
	model = Blog
	template_name = "main/deleteblog.html"
	success_url = reverse_lazy('main:allblogs')

class deleteCertificate(generic.DeleteView):
	model = Certificate
	template_name = "main/deleteCertificate.html"
	success_url = reverse_lazy('main:allcertificates')

class deleteContactView(generic.DeleteView):
	model = ContactProfile
	template_name = "main/deleteContactProfile.html"
	success_url = reverse_lazy('main:allContactProfiles')

class deleteMediaView(generic.DeleteView):
	model = Media
	template_name = "main/deleteMedia.html"
	success_url = reverse_lazy('main:allmedias')

class deletePortfolioView(generic.DeleteView):
	model = Portfolio
	template_name = "main/deletePortfolio.html"
	success_url = reverse_lazy('main:allportfolios')

class deleteSkillView(generic.DeleteView):
	model = Skill
	template_name = "main/deleteskills.html"
	success_url = reverse_lazy('main:allskills')

class deleteTestimonialView(generic.DeleteView):
	model = Testimonial
	template_name = "main/deleteTestimonial.html"
	success_url = reverse_lazy('main:alltestimonials')