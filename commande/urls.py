from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_commande),
    # Creer une vue pour ajouter les commandes
    path('/add_command', views.add_commande, name='add_command'),
    path('edit_command/<str:pk> ', views.edit_commande, name='edit_command'),
    path('delete_command/<str:pk> ', views.delete_commande, name='delete_command'),
]
 