from django.db import models

# Create your models here.
class Login_model(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

# class Route_model(models.Model):
#     source=models.CharField(max_length=100,null=True,blank=True)
#     destination=models.CharField(max_length=100,null=True,blank=True)