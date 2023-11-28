from django.forms import ModelForm
from .models import Commande


# relier notre modele au formulaire
class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields = '__all__'