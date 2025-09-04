from django.shortcuts import render
from django.http import HttpResponse

def home(request, param):
    return HttpResponse("<h1>Bonjour "+param+" !!!</h1>")

def home_sans_param(request):
    return HttpResponse("<h1>Bonjour !!!</h1>")

def about_us(request):
    return HttpResponse("<h1>About Us</h1>")

def contact_us(request):
    return HttpResponse("<h1>Contact Us</h1>")

# Create your views here.
