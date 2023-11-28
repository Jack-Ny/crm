from django.contrib import admin
from .models import Client

# Register your models here.
# permettre a client d'etre visible dans le page admin
admin.site.register(Client)