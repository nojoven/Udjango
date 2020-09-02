from django.db import models

# Create your models here.


class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # l'enregistrement du téléphone nécessite
    # un enregistrement auprès de la CNIL
    # phone = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    summary = models.TextField(max_length=200)
    previous_work = models.TextField(max_length=200)
    skills = models.TextField(max_length=200)



