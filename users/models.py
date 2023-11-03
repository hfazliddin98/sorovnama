from django.db import models



class Talaba(models.Model):
    login = models.CharField(max_length=255)
    parol = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    semestr_id = models.CharField(max_length=255)
    semestr_name = models.CharField(max_length=255)
    semestr_code = models.CharField(max_length=255)
    fakultet_id = models.CharField(max_length=255)
    fakultet_name = models.CharField(max_length=255)
    rasm = models.URLField(max_length=255 ,blank=True, null=True)