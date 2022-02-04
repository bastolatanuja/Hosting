from re import template
from unicodedata import name
from django.urls import path
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_view
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
	path('register/', views.RegisterView, name="register"),
	path('login/',views.login,name="login"),
	path('profile/',views.profileView,name="profile"),
	path('logout/',views.logout, name="logout"),
	path('editprofile/',views.editprofileView.as_view(),name="editprofile"),
	path('password/',views.PasswordsChangeView.as_view(template_name='main/change-password.html'),name="password"),
	path('changedp/',views.editDPView,name="changedp"),
	path('updateDP/',views.dpChangeView.as_view(),name="updateDP"),
	path('deletedp/',views.SetUserImageDefault,name="deletedp")
	]