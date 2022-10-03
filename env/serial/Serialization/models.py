from django.db import models

# Create your models here.
class Book(models.Model):
    name= models.CharField(max_length=200,primary_key=True);
    img = models.CharField(max_length=300);
    author= models.CharField(max_length=100);
    publisher= models.CharField(max_length=100);
    price= models.PositiveIntegerField(default=0);
# USER SCHEMA
class Users(models.Model):
    username = models.CharField(max_length=100,null=False,primary_key=True);
    email = models.EmailField(max_length=150,null=False);
    password = models.CharField(max_length=50,null=False);

