from pickle import TRUE
from django.db import models

# Create your models here.
class newuser(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)
    

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null='True')
    phone = models.CharField(max_length=10, null='True')
    desc = models.TextField(null='True')

class Hospital(models.Model):
    hname=models.CharField(max_length=250)
    address= models.CharField(max_length=540)
    area=models.CharField(max_length=90,null='True')
    ambno=models.CharField(max_length=250)
    dname=models.CharField(max_length=340)
    phone=models.CharField(max_length=120)
    

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bookambulance(models.Model):
    boolChoice = (
        ("M","Male"),("F","Female")
        )
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    hname=models.CharField(max_length=500 ,null='True')
    address=models.CharField(max_length=350)
    uphone=models.CharField(max_length=100)
    tambulance=models.CharField(max_length=90)
    age=models.CharField(max_length=3)
    gender = models.CharField(max_length = 1,choices=boolChoice)



    