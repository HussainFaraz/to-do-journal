from datetime import date
from django.db import models
from datetime import datetime


# Create your models here.

class ToDoDB(models.Model):
    task = models.CharField(max_length=50)


    def __str__(self):
        return "%s"%(self.task)
    

class User(models.Model):
    name = models.CharField(max_length=20)
    email =  models.EmailField(max_length=254)

    def __str__(self):
        return "%s%s"%(self.name,self.email)
