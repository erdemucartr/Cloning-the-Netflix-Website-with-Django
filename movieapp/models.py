from django.db import models
from autoslug import AutoSlugField
from user.models import *


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from= 'title',unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='movie-image')
    video = models.FileField(upload_to='movie-video')
    description = models.TextField(max_length=150, blank=True,null=True)
    slug = AutoSlugField(populate_from = 'title',unique=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
class Favoriler(models.Model):
    film = models.ForeignKey(Movie,  on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username