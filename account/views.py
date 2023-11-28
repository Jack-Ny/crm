from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUser
from django.contrib import messages

# Creer un compte
def registerPage(request):
    # creer un formulaire (il est deja preetabli par django)
    form = CreateUser()
    if request.method=='POST':
        form = CreateUser(request.POST)
        # si le formulaire est valide
        if form.is_valid():
            # On enregistre les donnees
            form.save()
            # creer un user
            user = form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a ete creer avec succes' + user )
            return redirect ('login')
    context = {
        'form' : form
    }
    return render(request, 'account/register.html', context)


# Se connecter
def loginPage(request):
    context = {
        
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Appeler la fontion authenticate (elle vas verifier si y'a correspondance entre les donnees)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, "Il y'a une erreur sur les informations entrees")
            
    return render(request, 'account/login.html', context)

# Se deconnecter
def logoutUser(request):
    logout(request)
    return redirect('login')
    