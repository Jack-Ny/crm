    from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required

# Create your views here.
# Ajouter une cle primaire pour pointer sur l'ID
@login_required(login_url='login')
def list_client(request, pk):
    # Obtenir l'id du client
    client = Client.objects.get(id=pk)
    # chercher les commandes d'un client
    commande = client.commande_set.all()
    commande_total = commande.count()
    myFilter = CommandeFiltre(request.GET, queryset=commande)
    # Mettre a jour les commandes
    commande = myFilter.qs
    
    context = {
        'client' : client,
        'commande' : commande,
        'commande_total' : commande_total,
        'myFilter' : myFilter
    }
    return render(request, 'client/list_client.html', context)
    
