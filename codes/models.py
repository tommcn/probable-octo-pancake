from django.db import models

# Create your models here.
class classe(models.Model):
    """
    A model for representing a class
    A class has a name, a group its assigned to, a teacher, a start and finish time and a zoom code
    """
    nom = models.CharField(max_length=127, help_text="Nom de la classe (matière)")
    classe_groupe = models.CharField(max_length=15, help_text="Classe concerné par le cours")
    prof = models.CharField(max_length=31)
    commnence = models.DateTimeField()
    fini = models.DateTimeField()
    code = models.BigIntegerField(help_text="Le code du cours pour Zoom")
    link = models.CharField(max_length=255)
    posted = models.BooleanField(default=False)
