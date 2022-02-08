from re import template
from unicodedata import name
from django.urls import path
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_view
from . import views
from .views import testView


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
	path('deletedp/',views.SetUserImageDefault,name="deletedp"),
	path('donate/',views.donate,name="donate"),
	path('adminpanel/',views.admin,name="adminpanel"),
	path('editsuperuser/',views.editprofileView.as_view(),name="editsuperuser"),
	path('allblogs/',views.allBlogsView.as_view(),name="allblogs"),
	path('allportfolios/',views.allPortfolioView.as_view(),name="allportfolios"),
	path('allcertificates/',views.testView.as_view(),name="allcertificates"),
	path('allcontactprofiles/',views.allcontactprofile,name="allcontactprofiles"),
	path('allskills/',views.allSkill.as_view(),name="allskills"),
	path('alltestimonials/',views.allTestimonial.as_view(),name="alltestimonials"),
	path('alluserprofiles/',views.allUserProfiles.as_view(),name="alluserprofiles"),
	path('allmedias/',views.allMedias.as_view(),name="allmedias"),
	path('addcertificate/',views.addCertificateView.as_view(),name="addcertificate"),
	path('addBlogs/',views.addBlogView.as_view(),name="addBlogs"),
	path('allContactProfiles/',views.allContactProfiles.as_view(),name="allContactProfiles"),
	path('contactDetails/<int:pk>',views.contactDetailView.as_view(),name="contactDetails"),
	path('addMedia/',views.addMediaView.as_view(),name="addMedia"),
	path('addPortfolio/',views.addPortfolio.as_view(),name="addPortfolio"),
	path('addSkill/',views.addSkill.as_view(),name="addSkill"),
	path('addTestimonial/',views.addTestimonial.as_view(),name="addTestimonial"),
	path('updateBlog/<int:pk>',views.updateBlogView.as_view(),name="updateBlog"),
	path('updateCertificate/<int:pk>',views.updateCertificateView.as_view(),name="updateCertificate"),
	path('updateMedia/<int:pk>',views.updateMedia.as_view(),name="updateMedia"),
	path('updatePortfolio/<int:pk>',views.updatePortfolio.as_view(),name="updatePortfolio"),
	path('updateSkill/<int:pk>',views.updateSkill.as_view(),name="updateSkill"),
	path('updateTestimonial/<int:pk>',views.updateTestimonial.as_view(),name="updateTestimonial"),
	path('updateUserProfile/<int:pk>',views.updateUserProfile.as_view(),name="updateUserProfile"),
	path('deleteBlog/<int:pk>',views.deleteBlogView.as_view(),name="deleteBlog"),
	path('deleteCertificate/<int:pk>',views.deleteCertificate.as_view(),name="deleteCertificate"),
	path('deleteContactProfile/<int:pk>',views.deleteContactView.as_view(),name="deleteContactProfile"),
	path('deleteMedia/<int:pk>',views.deleteMediaView.as_view(),name="deleteMedia"),
	path('deletePortfolio/<int:pk>',views.deletePortfolioView.as_view(),name="deletePortfolio"),
	path('deleteSkill/<int:pk>',views.deleteSkillView.as_view(),name="deleteSkill"),
	path('deleteTestimonial/<int:pk>',views.deleteTestimonialView.as_view(),name="deleteTestimonial"),
	]