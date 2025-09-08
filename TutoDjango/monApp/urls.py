from django.urls import path
from . import views

urlpatterns = [
path('home/<param>',views.home ,name='home'),
path('home',views.home_sans_param ,name='home'),
path("aboutus", views.about_us, name="aboutus"),
path("contactus", views.contact_us, name="contactus"),
path("produits", views.list_produits, name="produits"),
path("categories", views.list_categories, name="categories"),
path("statuts", views.list_statuts, name="statuts"),
]