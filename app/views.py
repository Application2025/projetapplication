from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plancomptable,Client,Fournisseur,Immobilisation, Tresorerie,Compte, Ecriture, Facture
from .forms import PlancomptableForm,ClientForm,FournisseurForm,ImmobilisationForm, TresorerieForm,CompteForm,EcritureForm, FactureForm


"""
def compte(request,pk):
        p=Plancomptable.objects.all()
        for p in p:
            p=p.id
            if(p==pk):
                break
        a=Compte.objects.all()
        form= CompteForm()
        if request.method == "POST":
            form=CompteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("compte")
        context={"comptes":a, "form":form,p:"p"}
        return render(request,"compte/compte.html", context)
"""
# Create your views here.
def home(request):
    return render(request,"home.html")

class Class_compte:
    def compte(request,pk):
        p=Plancomptable.objects.get(id=pk)
        a=Compte.objects.filter(plan_comptable=p)
        form= CompteForm(initial={'plan_comptable': p})
        if request.method == "POST":
            form=CompteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("compte", pk=pk)
        context={"comptes":a, "form":form, "p":p}
        return render(request,"compte/compte.html", context)

    def compte_delete(request, pk, iq):
        
        p=Plancomptable.objects.get(id=pk)
        a=Compte.objects.get(id=iq, plan_comptable=p)
        if request.method=="POST":
            a.delete()
            return redirect("compte", pk=pk)
        context={"elt":a,"p":p}
        return render(request,"compte/compte_delete.html",context)

    def compte_update(request,pk,iq):
        p=Plancomptable.objects.get(id=pk)
        a=Compte.objects.get(id=iq, plan_comptable=p)
        form=CompteForm(instance=a)
        if request.method=="POST":
            form=CompteForm(request.POST,instance=a)
            form.save()
            return redirect("compte", pk=pk)
        context={"form":form,"elt":a,"p":p}
        return render(request,"compte/compte_update.html",context)


class Class_plancomptable:
    def plancomptable(request):
        a=Plancomptable.objects.all()
        form= PlancomptableForm()
        if request.method == "POST":
            form=PlancomptableForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("plancomptable")
        context={"plancomptables":a, "form":form}
        return render(request,"plancomptable/plancomptable.html", context)

    def plancomptable_delete(request, pk):
        a=Plancomptable.objects.get(id=pk)
        if request.method=="POST":
            a.delete()
            return redirect("plancomptable")
        context={"elt":a}
        return render(request,"plancomptable/plancomptable_delete.html",context)

    def plancomptable_update(request,pk):
        a=Plancomptable.objects.get(id=pk)
        form=PlancomptableForm(instance=a)
        if request.method=="POST":
            form=PlancomptableForm(request.POST,instance=a)
            form.save()
            return redirect("plancomptable")
        context={"form":form,"elt":a}
        return render(request,"plancomptable/plancomptable_update.html",context)

class Class_ecriture:
    def ecriture(request):
        a= Ecriture.objects.select_related('debit', 'credit').all()
        form= EcritureForm()
        if request.method == "POST":
            form=EcritureForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("ecriture")
        context={"ecritures":a, "form":form}
        return render(request,"ecriture/ecriture.html", context)

    def ecriture_delete(request, pk):
        a=Ecriture.objects.get(id=pk)
        if request.method=="POST":          
            a.delete()
            return redirect("ecriture")
        context={"elt":a}
        return render(request,"ecriture/ecriture_delete.html",context)

    def ecriture_update(request,pk):
        a=Ecriture.objects.get(id=pk)
        form=EcritureForm(instance=a)
        if request.method=="POST":
            form=EcritureForm(request.POST,instance=a)
            form.save()
            return redirect("ecriture")
        context={"form":form,"elt":a}
        return render(request,"ecriture/ecriture_update.html",context)
    
class Class_facture:
    def facture(request):
        a= Facture.objects.select_related('client', 'fournisseur').all()
        form= FactureForm()
        if request.method == "POST":
            form=FactureForm(request.POST)
            if form.is_valid():
                form.save()
                redirect("facture")
        context={"factures":a, "form":form}
        return render(request,"facture/facture.html", context)

    def facture_delete(request, pk):
        a=Facture.objects.get(id=pk)
        if request.method=="POST":          
            a.delete()
            return redirect("facture")
        context={"elt":a}
        return render(request,"facture/facture_delete.html",context)

    def facture_update(request,pk):
        a=Facture.objects.get(id=pk)
        form=FactureForm(instance=a)
        if request.method=="POST":
            form=FactureForm(request.POST,instance=a)
            form.save()
            return redirect("facture")
        context={"form":form,"elt":a}
        return render(request,"facture/facture_update.html",context)

class Class_client:
    def client(request):
        a=Client.objects.all()
        form= ClientForm()
        if request.method == "POST":
            form=ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("client")
        context={"clients":a, "form":form}
        return render(request,"client/client.html", context)
    
    def client_delete(request, pk):
        a=Client.objects.get(id=pk)
        if request.method=="POST":
            a.delete()
            return redirect("client")
        context={"elt":a}
        return render(request,"client/client_delete.html",context)

    def client_update(request,pk):
        a=Client.objects.get(id=pk)
        form=ClientForm(instance=a)
        if request.method=="POST":
            form=ClientForm(request.POST,instance=a)
            form.save()
            return redirect("client")
        context={"form":form,"elt":a}
        return render(request,"client/client_update.html",context)

class Class_fournisseur:
    def fournisseur(request):
        a=Fournisseur.objects.all()
        form= FournisseurForm()
        if request.method == "POST":
            form=FournisseurForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("fournisseur")
        context={"fournisseurs":a, "form":form}
        return render(request,"fournisseur/fournisseur.html", context)
    
    def fournisseur_delete(request, pk):
        a=Fournisseur.objects.get(id=pk)
        if request.method=="POST":
            a.delete()
            return redirect("fournisseur")
        context={"elt":a}
        return render(request,"fournisseur/fournisseur_delete.html",context)

    def fournisseur_update(request,pk):
        a=Fournisseur.objects.get(id=pk)
        form=FournisseurForm(instance=a)
        if request.method=="POST":
            form=FournisseurForm(request.POST,instance=a)
            form.save()
            return redirect("fournisseur")
        context={"form":form,"elt":a}
        return render(request,"fournisseur/fournisseur_update.html",context)

class Class_immobilisation:
    def immobilisation(request):
        a=Immobilisation.objects.all()
        form= ImmobilisationForm()
        if request.method == "POST":
            form=ImmobilisationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("immobilisation")
        context={"immobilisations":a, "form":form}
        return render(request,"immobilisation/immobilisation.html", context)
    
    def immobilisation_delete(request, pk):
        a=Immobilisation.objects.get(id=pk)
        if request.method=="POST":
            a.delete()
            return redirect("immobilisation")
        context={"elt":a}
        return render(request,"immobilisation/immobilisation_delete.html",context)

    def immobilisation_update(request,pk):
        a=Immobilisation.objects.get(id=pk)
        form=ImmobilisationForm(instance=a)
        if request.method=="POST":
            form=ImmobilisationForm(request.POST,instance=a)
            form.save()
            return redirect("immobilisation")
        context={"form":form,"elt":a}
        return render(request,"immobilisation/immobilisation_update.html",context)

class Class_tresorerie:
    def tresorerie(request):
        a=Tresorerie.objects.all()
        form= TresorerieForm()
        if request.method == "POST":
            form=TresorerieForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("tresorerie")
        context={"tresoreries":a, "form":form}
        return render(request,"tresorerie/tresorerie.html", context)
    
    def tresorerie_delete(request, pk):
        a=Tresorerie.objects.get(id=pk)
        if request.method=="POST":
            a.delete()
            return redirect("tresorerie")
        context={"elt":a}
        return render(request,"tresorerie/tresorerie_delete.html",context)

    def tresorerie_update(request,pk):
        a=Tresorerie.objects.get(id=pk)
        form=TresorerieForm(instance=a)
        if request.method=="POST":
            form=TresorerieForm(request.POST,instance=a)
            form.save()
            return redirect("tresorerie")
        context={"form":form,"elt":a}
        return render(request,"tresorerie/tresorerie_update.html", context)