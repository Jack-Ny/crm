import django_filters
from .models import Commande


class CommandeFiltre(django_filters.FilterSet):
    # Faire le lien entre notre filtre et les commandes
    class Meta:
        model = Commande
        fields = '__all__'
        exclude = ['date_creation', 'client']