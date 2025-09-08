from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Statut, Categorie

def home(request, param):
    return HttpResponse("<h1>Bonjour "+param+" !!!</h1>")

def home_sans_param(request):
    return HttpResponse("<h1>Bonjour !!!</h1>")

def about_us(request):
    return HttpResponse("<h1>About Us</h1>")

def contact_us(request):
    return HttpResponse("<h1>Contact Us</h1>")

def list_produits(request):
    prdts = Produit.objects.all()
    produit_html = ""
    for prdt in prdts:
        produit_html+=f"<li>{prdt.intituleProd}</li>\n"

    html= f"""
    <h1> Produits </h1>
    <ul> 
        {produit_html}
    </ul>
    """

    return HttpResponse(html)

def list_statuts(request):
    statuts = Statut.objects.all()
    statut_html = ""
    for s in statuts:
        statut_html+=f"<li>{s.libelle}</li>\n"

    html= f"""
    <h1> Produits </h1>
    <ul> 
        {statut_html}
    </ul>
    """

    return HttpResponse(html)


def list_categories(request):
    ctgrs = Categorie.objects.all()
    categorie_html = ""
    for ctgr in ctgrs:
        categorie_html+=f"<li>{ctgr.nomCat}</li>\n"

    html= f"""
    <h1> Produits </h1>
    <ul> 
        {categorie_html}
    </ul>
    """

    return HttpResponse(html)



# Create your views here.
