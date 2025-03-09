from django.urls import path
from . import views
from .views import Class_client,Class_compte,Class_plancomptable, Class_fournisseur, Class_immobilisation, Class_tresorerie,Class_ecriture,Class_facture

urlpatterns=[
    path("", views.home, name="home"),
    path("plancomptable/", Class_plancomptable.plancomptable, name="plancomptable"),
    path("plancomptable/<int:pk>/plancomptable_delete", Class_plancomptable.plancomptable_delete, name="plancomptable_delete"),
    path("plancomptable/<int:pk>/plancomptable_update", Class_plancomptable.plancomptable_update, name="plancomptable_update"),
    path("plancomptable/<int:pk>/compte", Class_compte.compte, name="compte"),
    path("plancomptable/<int:pk>/compte/<int:iq>/compte_delete", Class_compte.compte_delete, name="compte_delete"),
    path("plancomptable/<int:pk>/compte/<int:iq>/compte_update", Class_compte.compte_update, name="compte_update"),
    path("client/", Class_client.client, name="client"),
    path("client/<int:pk>/client_delete", Class_client.client_delete, name="client_delete"),
    path("client/<int:pk>/client_update", Class_client.client_update, name="client_update"),
    path("fournisseur/", Class_fournisseur.fournisseur, name="fournisseur"),
    path("fournisseur/<int:pk>/fournisseur_delete", Class_fournisseur.fournisseur_delete, name="fournisseur_delete"),
    path("fournisseur/<int:pk>/fournisseur_update", Class_fournisseur.fournisseur_update, name="fournisseur_update"),
    path("immobilisation/", Class_immobilisation.immobilisation, name="immobilisation"),
    path("immobilisation/<int:pk>/immobilisation_delete", Class_immobilisation.immobilisation_delete, name="immobilisation_delete"),
    path("immobilisation/<int:pk>/immobilisation_update", Class_immobilisation.immobilisation_update, name="immobilisation_update"),
    path("tresorerie/", Class_tresorerie.tresorerie, name="tresorerie"),
    path("tresorerie/<int:pk>/tresorerie_delete", Class_tresorerie.tresorerie_delete, name="tresorerie_delete"),
    path("tresorerie/<int:pk>/tresorerie_update", Class_tresorerie.tresorerie_update, name="tresorerie_update"),
    path("ecriture/", Class_ecriture.ecriture, name="ecriture"),
    path("ecriture/<int:pk>/ecriture_delete", Class_ecriture.ecriture_delete, name="ecriture_delete"),
    path("ecriture/<int:pk>/ecriture_update", Class_ecriture.ecriture_update, name="ecriture_update"),
    path("facture/", Class_facture.facture, name="facture"),
    path("facture/<int:pk>/facture_delete", Class_facture.facture_delete, name="facture_delete"),
    path("facture/<int:pk>/facture_update", Class_facture.facture_update, name="facture_update"),


]