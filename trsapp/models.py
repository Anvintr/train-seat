from django.db import models

# Create your models here.
class Login_model(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

# class Route_model(models.Model):
#     source=models.CharField(max_length=100,null=True,blank=True)
#     destination=models.CharField(max_length=100,null=True,blank=True)


class user_model(models.Model):
    LOGINID=models.ForeignKey(Login_model,on_delete=models.CASCADE,null=True,blank=True)
    Fullname=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    aadharnumber=models.CharField(max_length=100,null=True,blank=True)


class complaint_model(models.Model):
    USER_ID=models.ForeignKey(user_model,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.CharField(max_length=100,null=True,blank=True)
    reply=models.CharField(max_length=100,null=True,blank=True)


class feedback_model(models.Model):
    USER_ID=models.ForeignKey(user_model,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)
    rating=models.CharField(max_length=100,null=True,blank=True)

