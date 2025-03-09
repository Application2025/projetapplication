# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'client'
    def __str__(self):
        return f" {self.nom}"



class Compte(models.Model):
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    numero = models.CharField(unique=True, max_length=50)
    solde = models.DecimalField(max_digits=18, decimal_places=2)
    plan_comptable = models.ForeignKey('Plancomptable', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'compte'
    def __str__(self):
        return f"{self.numero} - {self.nom}"

        


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ecriture(models.Model):
    date = models.DateField()
    montant = models.DecimalField(max_digits=18, decimal_places=2)
    commentaire = models.TextField(blank=True, null=True)
    justificatif = models.CharField(max_length=255, blank=True, null=True)
    debit = models.ForeignKey(Compte, models.DO_NOTHING)
    credit = models.ForeignKey(Compte, models.DO_NOTHING, related_name='ecriture_credit_set')

    class Meta:
        managed = True
        db_table = 'ecriture'
    def __str__(self):
        return f" {self.id}-{self.date}"


class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fournisseur'
    def __str__(self):
        return f"{self.nom}"


class Facture(models.Model):
    numero = models.CharField(max_length=50)
    date_emission = models.DateField()
    date_echeance = models.DateField()
    montant_total = models.DecimalField(max_digits=18, decimal_places=2)
    etat = models.CharField(max_length=50)
    client = models.ForeignKey(Client, models.DO_NOTHING, blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'facture'
    def __str__(self):
        return f" {self.id}-{self.numero}"

class Notification(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    date_envoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20)


class Immobilisation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date_acquisition = models.DateField()
    valeur_acquisition = models.DecimalField(max_digits=18, decimal_places=2)
    duree_de_vie = models.IntegerField()
    taux_amortissement = models.DecimalField(max_digits=5, decimal_places=4)
    valeur_residuelle = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'immobilisation'
    def __str__(self):
        return f" {self.id}-{self.nom}"


class Plancomptable(models.Model):
    nom = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plancomptable'
    def __str__(self):
        return f" {self.id}-{self.nom}"


class Tresorerie(models.Model):
    date = models.DateField()
    flux = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=18, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tresorerie'

    def __str__(self):
        return f" {self.id}-{self.date}"


