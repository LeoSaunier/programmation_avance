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
