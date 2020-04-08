from django.db import models

# Create your models here.
class classe(models.Model):
    nom = models.CharField(max_length=127)
    classe_groupe = models.CharField(max_length=2)
    prof = models.CharField(max_length=31)
    commnence = models.DateTimeField()
    fini = models.DateTimeField()
    code = models.IntegerField()
    link = models.CharField(max_length=255)
