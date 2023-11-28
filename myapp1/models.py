from django.db import models

# Create your models here.

class ContactList(models.Model):
    id =  models.IntegerField(default=0, primary_key= True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    telephone = models.IntegerField(default=0)
    email = models.CharField(max_length=200)
    birthday = models.DateTimeField()