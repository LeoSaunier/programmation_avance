from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
path("home/<param>", views.HomeView.as_view(), name='home'),
##path('home',views.home_sans_param ,name='home'),
path("aboutus", views.AboutView.as_view(), name="aboutus"),
path("contactus", views.ContactView, name="contactus"),
##path("produits", views.ListProduits, name="produits"),
path("categories/", views.CategorieListView.as_view(), name="lst_ctgrs"),
path("categorie/<pk>/", views.CategorieDetailView.as_view(), name="dtl_ctgr"),
path("home/", views.HomeView.as_view(), name='home'),
path("produits/",views.ProduitListView.as_view(),name="lst_prdts"),
path("produit/<pk>/" ,views.ProduitDetailView.as_view(), name="dtl_prdt"),
path("statuts/", views.StatutListView.as_view(), name="lst_stts"),
path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_stt"),
path("rayons/", views.RayonListView.as_view(), name="lst_rayons"),
path("rayon/<pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),
path('login/', views.ConnectView.as_view(), name='login'),
path('register/', views.RegisterView.as_view(), name='register'),
path('logout/', views.DisconnectView.as_view(), name='logout'),
path('email-sent/', views.EmailSentView, name='email-sent'),
]