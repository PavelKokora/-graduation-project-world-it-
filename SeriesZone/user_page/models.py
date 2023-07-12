from django.db import models
from django.contrib.auth.models import User
from catalog.models import *
# Create your models here.

class My_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serial = models.ManyToManyField(Serial)
    
# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     serial = models.ManyToManyField(Serial)
