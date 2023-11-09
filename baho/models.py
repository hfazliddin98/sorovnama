from django.db import models
from django.urls import reverse
from users.models import Kurs



class Fanlar(models.Model):   
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    
class Turlar(models.Model):   
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    
class Oqituvchilar(models.Model):   
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name  
    

class Fan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)   
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    
class Tur(models.Model):  
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)    
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name
    
class Oqituvchi(models.Model):  
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)    
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
    tur = models.ForeignKey(Turlar, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)

    def __str__(self):        
        return self.name  
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"fan": self.fan, "tur":self.tur})


    
class Umumiy(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)    
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
    tur = models.ForeignKey(Turlar, on_delete=models.CASCADE)
    oqituvchi = models.ForeignKey(Oqituvchilar, on_delete=models.CASCADE)
    baza = models.CharField(max_length=10, default=0)

    def __str__(self):
        name = f'{self.id}'
        return name
    

class Sorovnoma(models.Model):
    umumiy = models.ForeignKey(Umumiy, on_delete=models.CASCADE)
    baho = models.CharField(max_length=255)
    baza = models.CharField(max_length=10, blank=True, null=True, default=0)

    def __str__(self):
        return self.baho
    
class Baza(models.Model):
    kurs = models.CharField(max_length=255)    
    fan = models.CharField(max_length=255)
    tur = models.CharField(max_length=255)
    oqtuvchi = models.CharField(max_length=255)
    baho = models.CharField(max_length=255)

    def __str__(self):
        return self.baho