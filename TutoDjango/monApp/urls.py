from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
path("home/<param>", views.HomeView.as_view(), name='accueil'),
##path('home',views.home_sans_param ,name='home'),
path("aboutus", views.AboutView.as_view(), name="aboutus"),
path("contactus", views.ContactView.as_view(), name="contactus"),
##path("produits", views.ListProduits, name="produits"),
path("categories", views.list_categories, name="categories"),
path("statuts", views.list_statuts, name="statuts"),
path("rayons", views.list_rayons, name="rayons"),
path("home/", views.HomeView.as_view()),
path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
]