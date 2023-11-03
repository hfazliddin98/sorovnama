from django.db import models


class Kurs(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Guruh(models.Model):
    kurs_id = models.OneToOneField(Kurs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name