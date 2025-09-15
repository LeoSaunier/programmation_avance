from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Produit, Statut, Categorie

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def home_sans_param(request):
    if request.GET and request.GET["test"]:
        raise Http404
    return HttpResponse("Bonjour Monde!")

def about_us(request):
    return HttpResponse("<h1>About Us</h1>")

def contact_us(request):
    return HttpResponse("<h1>Contact Us</h1>")

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'premier_produit': prdts[0]})

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
