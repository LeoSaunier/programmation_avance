from django.urls import path
from . import views

urlpatterns = [
path("", views.home, name="home"),
path("aboutus", views.about_us, name="aboutus"),
path("contactus", views.contact_us, name="contactus"),
]