from django.contrib import admin
from .models import Client, Fournisseur,Plancomptable,Compte,Tresorerie,Immobilisation,Facture,Ecriture

# Register your models here.

admin.site.register(Client)
admin.site.register(Compte)
admin.site.register(Facture)
admin.site.register(Fournisseur)
admin.site.register(Plancomptable)
admin.site.register(Tresorerie)
admin.site.register(Immobilisation)
admin.site.register(Ecriture)