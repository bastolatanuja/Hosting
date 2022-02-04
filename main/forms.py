from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import ContactProfile,User, UserProfile



class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)

class editprofileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email',)
	password=None
	first_name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	last_name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	username = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class' :'form-control'
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.EmailInput(attrs={
			'class' :'form-control'
			}))
	
	
class changeDpForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'