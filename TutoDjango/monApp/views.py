from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Produit, Statut, Categorie, Rayon
from django.views.generic import *


def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

##def home_sans_param(request):
##    if request.GET and request.GET["test"]:
##        raise Http404
##    return HttpResponse("Bonjour Monde!")

def about_us(request):
    return render(request, 'monApp/about_us.html')

def contact_us(request):
    return render(request, 'monApp/contact_us.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'prdts': prdts})

def list_statuts(request):
    statuts = Statut.objects.all()
    return render(request, 'monApp/list_statuts.html', {'stts': statuts})


def list_categories(request):
    ctgrs = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'ctgrs': ctgrs})


def list_rayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rayons': rayons})
# Create your views here.

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['titreh1'] = "Hello DJANGO"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)