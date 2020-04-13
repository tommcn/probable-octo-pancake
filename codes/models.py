from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


# pylint: disable=no-member

# Create your models here.
GROUPES_CHOICES = [
    ("TOUS","Tous"),
    ("3R","3R"),
    ("3V","3V"),
    ("3B","3B"),
    ("3LATIN","3Latin"),
    ("3L&L1","3L&L1"),
    ("3L&L2","3L&L2"),
    ("3INTERMEDIATE1","3Intermediate1"),
    ("3INTERMEDIATE2","3Intermediate2"),
    ("3GROUPE1","3Groupe1"),
    ("3GROUPE2","3Groupe2"),
    ("3GROUPE3","3Groupe3"),
    ("3GROUPE4","3Groupe4"),
    ("3GROUPEART1","3GroupeArt1"),
    ("3GROUPEART2","3GroupeArt2"),
    ("3GROUPEART3","3GroupeArt3"),
    ("3GROUPEART4","3GroupeArt4"),
]

class classe(models.Model):
    """
    A model for representing a class
    A class has a name, a group its assigned to, a teacher, a start and finish time and a zoom code
    """
    nom = models.CharField(max_length=127, help_text="Nom de la classe (matière)")
    classe_groupe = models.CharField(max_length=15, help_text="Classe concerné par le cours", choices=GROUPES_CHOICES)
    prof = models.CharField(max_length=31)
    commnence = models.DateTimeField()
    fini = models.DateTimeField()
    code = models.BigIntegerField(help_text="Le code du cours pour Zoom")
    link = models.CharField(max_length=255)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Profile(models.Model):
    """
    A model for representing a user profile
    Links to an user
    Contains class subscribed to
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed_to = models.ManyToManyField(classe, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()