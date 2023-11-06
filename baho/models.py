from django.db import models
from users.models import Kurs


class Fan(models.Model):  
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)  
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    
    
class Turi(models.Model):    
    fan_id = models.ForeignKey(Fan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


    
class Oqtuvchi(models.Model):
    kurs_id = models.ForeignKey(Kurs, on_delete=models.CASCADE)    
    fan_id = models.ForeignKey(Fan, on_delete=models.CASCADE)
    tur_id = models.ForeignKey(Turi, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    

class Sorovnoma(models.Model):
    oqtuvchi_id = models.ForeignKey(Oqtuvchi, on_delete=models.CASCADE)
    baho = models.CharField(max_length=255)

    def __str__(self):
        return self.baho