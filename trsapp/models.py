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


class Route_model(models.Model):
    source=models.CharField(max_length=100,null=True,blank=True)
    destination=models.CharField(max_length=100,null=True,blank=True)


class Train_model(models.Model):
    ROUTE_ID=models.ForeignKey(Route_model,on_delete=models.CASCADE,null=True,blank=True)
    train_number=models.CharField(max_length=100,null=True,blank=True)
    train_name=models.CharField(max_length=100,null=True,blank=True)    

    
class Compartment_model(models.Model):
    TRAIN_ID=models.ForeignKey(Train_model,on_delete=models.CASCADE,null=True,blank=True)
    compartment_name=models.CharField(max_length=100,null=True,blank=True)
    compartment_type=models.CharField(max_length=100,null=True,blank=True)

class Station_model(models.Model):
    ROUTE_ID=models.ForeignKey(Route_model,on_delete=models.CASCADE,null=True,blank=True)
    station_name=models.CharField(max_length=100,null=True,blank=True)

class Seat_model(models.Model):
    COMPARTMENT_ID=models.ForeignKey(Compartment_model,on_delete=models.CASCADE,null=True,blank=True)
    seat_number=models.CharField(max_length=100,null=True,blank=True)
    seat_status=models.CharField(max_length=100,null=True,blank=True)
    TRAIN_ID=models.ForeignKey(Train_model,on_delete=models.CASCADE,null=True,blank=True)
    seat_type=models.CharField(max_length=100,null=True,blank=True)
    compartment_type=models.ForeignKey(complaint_model,on_delete=models.CASCADE,null=True,blank=True)

class Status_model(models.Model):
    TRAIN_ID=models.ForeignKey(Train_model,on_delete=models.CASCADE,null=True,blank=True)
    STATION_ID=models.ForeignKey(Station_model,on_delete=models.CASCADE,null=True,blank=True)
    arrival=models.CharField(max_length=100,null=True,blank=True)
    departure=models.CharField(max_length=100,null=True,blank=True)

class Booking_model(models.Model):
    USER_ID=models.ForeignKey(user_model,on_delete=models.CASCADE,null=True,blank=True)
    TRAIN_ID=models.ForeignKey(Train_model,on_delete=models.CASCADE,null=True,blank=True)
    COMPARTMENT_ID=models.ForeignKey(Compartment_model,on_delete=models.CASCADE,null=True,blank=True)
    SOURCE=models.CharField(max_length=100,null=True,blank=True)
    DESTINATION=models.CharField(max_length=100,null=True,blank=True)
    SEAT_NO=models.ForeignKey(Seat_model,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateField(auto_now_add=True)

class Alert_model(models.Model):
    USER_ID=models.ForeignKey(user_model,on_delete=models.CASCADE,null=True,blank=True)
    seat_no=models.ForeignKey(Seat_model,on_delete=models.CASCADE,null=True,blank=True)
    COMPARTMENT_ID=models.ForeignKey(Compartment_model,on_delete=models.CASCADE,null=True,blank=True)
    alertmsg=models.CharField(max_length=100,null=True,blank=True)
    extrainfo=models.CharField(max_length=100,null=True,blank=True)

