# tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Notification, Facture


@shared_task
def check_paiements():
    factures = Facture.objects.filter(
        date_echeance__lt=timezone.now(),
        etat='impayé'
    )
    for facture in factures:
        Notification.objects.create(
            facture=facture,
            statut='relance'
        )