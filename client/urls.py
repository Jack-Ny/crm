from django.urls import path
from . import views


urlpatterns = [
    
    # Je donne un nom pour pouvoir l'utiliser comme liens dynamique
    path('/<str:pk>', views.list_client, name='client'),
]
