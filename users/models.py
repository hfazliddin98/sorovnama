from django.db import models
from django.contrib.auth.models import AbstractUser



class Kurs(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, default='1-kurs')