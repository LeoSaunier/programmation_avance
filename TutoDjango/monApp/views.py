from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, Http404

from monApp.forms import *
from .models import Produit, Statut, Categorie, Rayon
from django.views.generic import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.db.models import Count, Prefetch
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

##def accueil(request,param):
##    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

##def home_sans_param(request):
##    if request.GET and request.GET["test"]:
##        raise Http404
##    return HttpResponse("Bonjour Monde!")

##def about_us(request):
##    return render(request, 'monApp/about_us.html')
##
##def contact_us(request):
##    return render(request, 'monApp/contact_us.html')

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
        if self.kwargs.get('param')!=None:
            context['titreh1'] = "Hello "+self.kwargs.get('param')
        else:
            context['titreh1'] = "Hello DJango"
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

##class ContactView(TemplateView):
##    template_name = "monApp/page_home.html"
##    def get_context_data(self, **kwargs):
##        context = super(ContactView, self).get_context_data(**kwargs)
##        context['titreh1'] = "Contact us..."
##        return context
##    def post(self, request, **kwargs):
##        return render(request, self.template_name)
    
class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('statut')
        # Charge les catégories et les statuts en même temps
        return Produit.objects.select_related('categorie').select_related('statut')
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context


class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"
    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context


class CategorieListView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "ctgrs"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Categorie.objects.filter(nomCat__icontains=query).annotate(nb_produits=Count('produits'))
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(CategorieListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Catégories"
        return context


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "ctgr"

    def get_queryset(self):
        # Annoter chaque catégorie avec le nombre de produits liés
        return Categorie.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la Catégorie"
        context['prdts'] = self.object.produits.all()
        return context


class StatutListView(ListView):
    model = Statut
    template_name = "monApp/list_statuts.html"
    context_object_name = "stts"

    def get_queryset(self):
        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Statut.objects.filter(libelle__icontains=query).annotate(nb_produits=Count('produits'))
        # Annoter chaque catégorie avec le nombre de produits liés
        return Statut.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(StatutListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Statuts"
        return context


class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stt"

    def get_queryset(self):
        # Annoter chaque statut avec le nombre de produits liés
        return Statut.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la Statut"
        context['prdts'] = self.object.produits.all()
        return context


class RayonListView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

    def get_queryset(self):

        # Surcouche pour filtrer les résultats en fonction de la recherche
        # Récupérer le terme de recherche depuis la requête GET
        query = self.request.GET.get('search')
        if query:
            return Rayon.objects.filter(nomRayon__icontains=query).prefetch_related(
        Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit"))
        )
        # Précharge tous les "contenir" de chaque rayon,
        # et en même temps le produit de chaque contenir
        return Rayon.objects.prefetch_related(
        Prefetch("contenir_rayon", queryset=Contenir.objects.select_related("produit"))
        )

    def get_context_data(self, **kwargs):
        context = super(RayonListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes Rayons"
        ryns_dt = []
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenir_rayon.all():
                total += contenir.produit.prixUnitaireProd * contenir.Qte
            ryns_dt.append({'rayon': rayon,'total_stock': total})
        context['ryns_dt'] = ryns_dt
        return context


class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"
    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la Rayon"

        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0
        
        for contenir in self.object.contenir_rayon.all():
            total_produit = contenir.produit.prixUnitaireProd * contenir.Qte
            prdts_dt.append({ 'produit': contenir.produit,
                'qte': contenir.Qte,
                'prix_unitaire': contenir.produit.prixUnitaireProd,
                'total_produit': total_produit} )
            total_rayon += total_produit
            total_nb_produit += contenir.Qte

        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context


class ConnectView(LoginView):
    template_name = 'monApp/page_login.html'
    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')


class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')
                

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)


def ContactView(request):
    titreh1 = "Contact us !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@monApp.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})


def EmailSentView(request):
    return render(request, "monApp/email_sent.html")

@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)


@method_decorator(login_required, name='dispatch')
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/update_produit.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')


@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_statut.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stt = form.save()
        return redirect('dtl_stt', stt.idStatut)


@method_decorator(login_required, name='dispatch')
class StatutUpdateView(UpdateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/update_statut.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        stt = form.save()
        return redirect('dtl_stt', stt.idStatut)


@method_decorator(login_required, name='dispatch')
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('lst_stts')


@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ctrg = form.save()
        return redirect('dtl_ctgr', ctrg.idCat)
    

@method_decorator(login_required, name='dispatch')
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/update_categorie.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        ctrg = form.save()
        return redirect('dtl_ctgr', ctrg.idCat)


@method_decorator(login_required, name='dispatch')
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_ctgrs')


@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)
    

@method_decorator(login_required, name='dispatch')
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/update_rayon.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = form.save()
        return redirect('dtl_rayon', rayon.idRayon)


@method_decorator(login_required, name='dispatch')
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')


class ContenirCreateView(CreateView):
    model = Contenir
    form_class=ContenirForm
    template_name = "monApp/create_contenir.html"

    def get_context_data(self, **kwargs):
        context= super(ContenirCreateView, self).get_context_data(**kwargs)
        context["rayon"]= Rayon.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = Rayon.objects.get(pk=self.kwargs["pk"])
        produit = form.cleaned_data["produit"]
        Qte = form.cleaned_data["Qte"]

        
        if Contenir.objects.filter(produit=produit, rayon=rayon).exists():
            contenir = Contenir.objects.get(produit=produit, rayon=rayon)
            contenir.Qte +=Qte
        else:
            contenir = Contenir.objects.create(rayon=rayon,produit=produit,Qte=Qte)
        
        contenir.save()

        return redirect('dtl_rayon', self.kwargs["pk"])
    
class ContenirUpdateView(UpdateView):
    model = Contenir
    form_class=ContenirForm
    template_name = "monApp/update_contenir.html"

    def get_context_data(self, **kwargs):
        context= super(ContenirUpdateView, self).get_context_data(**kwargs)
        context["rayon"]= Rayon.objects.get(pk=self.kwargs["pk"])
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Désactiver le champ 'produit' uniquement ici
        form.fields['produit'].disabled = True
        return form

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        rayon = Rayon.objects.get(pk=self.kwargs["pk"])
        produit = form.cleaned_data["produit"]
        Qte = form.cleaned_data["Qte"]

        
        if Qte<=0:
            contenir = Contenir.objects.get(produit=produit, rayon=rayon).delete()
        else:
            contenir = Contenir.objects.get(rayon=rayon,produit=produit)
            contenir.Qte = Qte
        
        contenir.save()

        return redirect('dtl_rayon', self.kwargs["pk"])
    
