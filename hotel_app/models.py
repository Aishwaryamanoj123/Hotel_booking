from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rooms(models.Model):
    image = models.ImageField(upload_to='static/img')
    room_name = models.CharField(max_length=50)
    price = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()
    wifi = models.CharField(max_length=50,default='')
   
    description = models.TextField()

    def __str__(self):
        return self.room_name



  
class CustomerDetails(models.Model):
    cid=models.IntegerField(primary_key=True)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    age=models.BigIntegerField()
    adhar=models.BigIntegerField()
    address=models.TextField()
    email=models.EmailField()
    phnno=models.BigIntegerField()
    user= models.ForeignKey(User,on_delete=models.CASCADE)





class AddRoom(models.Model):
    rno= models.IntegerField()
    des= models.TextField(max_length=100)
    ac=models.BooleanField()
    roomtype=models.CharField(max_length=100)
    bedtype=models.CharField(max_length=100)
    rate=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='static/img')
    status=models.BooleanField(default=True)
    

class Book(models.Model):
    checkin= models.DateField()
    checkout=models.DateField()
    amount=models.FloatField()
    customer= models.ForeignKey(to=CustomerDetails,on_delete=models.CASCADE)
    room= models.ForeignKey(to=AddRoom,on_delete=models.CASCADE)
