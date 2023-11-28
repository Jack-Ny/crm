from django.shortcuts import render
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    # recuperer tout les commandes et clients present dans la base
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    
    # Mettres les commandes et clients dans un dictionnaire
    context = {
        'commandes' : commandes,
        'clients'   : clients
    }
    
    return render(request, 'produit/acceuil.html', context)
