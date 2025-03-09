from django import forms
from .models import Client, Compte, Ecriture, Facture, Fournisseur, Immobilisation, Plancomptable, Tresorerie

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'adresse', 'email', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompteForm(forms.ModelForm):
    class Meta:
        CHOICES = [
        ('Actif', 'Actif'),
        ('Passif', 'Passif'),
        ('Capitaux propres', 'Capitaux propres'),
        ]
        model = Compte
        fields = ['nom', 'type', 'numero', 'solde', 'plan_comptable']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'solde': forms.NumberInput(attrs={'class': 'form-control'}),
            'plan_comptable': forms.Select(attrs={'class': 'form-control'}),
        }

class EcritureForm(forms.ModelForm):
    class Meta:
        model = Ecriture
        fields = ['date', 'montant', 'commentaire', 'justificatif', 'debit', 'credit']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'justificatif': forms.TextInput(attrs={'class': 'form-control'}),
            'debit': forms.Select(attrs={'class': 'form-control'}),
            'credit': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'debit': 'Compte Débiteur',
            'credit': 'Compte Créditeur'
        }
    def clean_montant(self):
        montant = self.cleaned_data['montant']
        if montant <= 0:
            raise forms.ValidationError("Le montant doit être positif")
        return montant

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['debit'].queryset = Compte.objects.filter(type='Actif')
            self.fields['credit'].queryset = Compte.objects.filter(type='Passif')

        
class FactureForm(forms.ModelForm):
    class Meta:
        CHOICES=[
            ('Non payé','Non payé'), 
            ('Partiellement payé','Partiellement payé'), 
            ('Payé','Payé',),
        ]
        model = Facture
        fields = ['numero', 'date_emission', 'date_echeance', 'montant_total', 'etat', 'client', 'fournisseur']
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'date_emission': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_echeance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'},choices=CHOICES),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'fournisseur': forms.Select(attrs={'class': 'form-control'}),
        }
    def clean_montant(self):
        montant = self.cleaned_data['montant_total']
        if montant <= 0:
            raise forms.ValidationError("Le montant doit être positif")
        return montant
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['client'].queryset = Client.objects.filter()
            self.fields['fournisseur'].queryset = Fournisseur.objects.filter()

        
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'adresse', 'email', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ImmobilisationForm(forms.ModelForm):
    class Meta:
        model = Immobilisation
        fields = ['nom', 'description', 'date_acquisition', 'valeur_acquisition', 
                 'duree_de_vie', 'taux_amortissement', 'valeur_residuelle']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_acquisition': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'valeur_acquisition': forms.NumberInput(attrs={'class': 'form-control'}),
            'duree_de_vie': forms.NumberInput(attrs={'class': 'form-control'}),
            'taux_amortissement': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001'}),
            'valeur_residuelle': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    

class PlancomptableForm(forms.ModelForm):
    class Meta:
        model = Plancomptable
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class TresorerieForm(forms.ModelForm):
    class Meta:
        CHOICES = [
        ('Entrée', 'Entrée'),
        ('Sortie', 'Sortie'),
]
        model = Tresorerie
        fields = ['date', 'flux', 'montant', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'flux': forms.Select(attrs={'class': 'form-control'},choices=CHOICES),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    def clean_montant(self):
        montant = self.cleaned_data['montant']
        if montant <= 0:
            raise forms.ValidationError("Le montant doit être positif")
        return montant