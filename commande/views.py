from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CommandeForm
from .models import Commande
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def list_commande(request):
    return render(request, 'commande/list_commande.html')
    
@login_required(login_url='login')
def add_commande(request):
    # Appeler notre formulaire dans la vue
    # Et definir la sauvegarde et l'enregistrement des donnees
    form = CommandeForm()
    if request.method=='POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form
    }  
    return render (request, 'commande/add_commande.html', context)

@login_required(login_url='login')
def edit_commande(request, pk):
    # Chercher d'abord la commande a modifier
    commande = Commande.objects.get(id=pk)
    # Ici c'est un formulaire qui contient deja des commandes a modifier (d'ou le parametre instance)
    # Instnace prend la commande contenant l'ID a modifier
    form = CommandeForm(instance=commande)
  
    if request.method=='POST':
        form = CommandeForm(request.POST, instance=commande) # ajouter l'instance    
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form
    }
    return render (request, 'commande/add_commande.html', context)

@login_required(login_url='login')
def delete_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    if request.method=='POST':
        commande.delete()
        return redirect('/')
    context = {
        'item' : commande # pour eviter la confusion avec form
    }
    return render(request, 'commande/delete_commande.html', context)