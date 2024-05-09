from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=11)

    
class Profil(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profil-resim')
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.title