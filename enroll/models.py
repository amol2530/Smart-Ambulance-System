from pickle import TRUE
from random import choices
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
    names = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null='True')
    phone = models.CharField(max_length=10, null='True')
    desc = models.TextField(null='True')
    var = models.TextField(null='True')
    var2 = models.TextField(null='True')

class Hospital(models.Model):
    hname=models.CharField(max_length=250)
    address= models.CharField(max_length=540)
    area=models.CharField(max_length=90,null='True')
    ambno=models.CharField(max_length=250)
    dname=models.CharField(max_length=340)
    phone=models.CharField(max_length=120)

    def __str__(self):
        return self.hname
    

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Area(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default = '0')
    fac1=models.CharField(max_length=120,default = '0')
    fac2=models.CharField(max_length=120,default = '0')
    fac3=models.CharField(max_length=120,default = '0')
    fac4=models.CharField(max_length=120,default = '0')

    def __str__(self):
        return self.name

class Bookambulance(models.Model):
    # hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE,null='True')
    boolChoice = (
        ("1","Male"),("2","Female")
        )
    SEMESTER_CHOICES = (
        ("1", "Basic Ambulance"),
        ("2", "Advance Ambulance"),
        ("3", "Mortuary Ambulance"),
        ("4", "Patient Transport Vehicle"),
        ("5", "Air Ambulance"),
     
        )
    fname=models.CharField(max_length=90)
    lname=models.CharField(max_length=90)
    hname=models.CharField(max_length=90,null='True')
    address=models.CharField(max_length=350)
    uphone=models.CharField(max_length=100)
    tambulance = models.CharField(max_length = 20,choices = SEMESTER_CHOICES,default = '0')
    age=models.CharField(max_length=3)
    gender = models.CharField(max_length = 1,choices=boolChoice,default = '0')


class Hospitaldetails(models.Model):
    SEMESTER_CHOICES = (
        ("1", "Private"),
        ("2", "goverments"),
    )
    hname=models.CharField(max_length=250)
    htype = models.CharField(max_length = 20,choices = SEMESTER_CHOICES,default = '0')
    haddress=models.CharField(max_length=350)
    hcontact=models.CharField(max_length=450)
    hemail=models.CharField(max_length=150)
    ambno=models.CharField(max_length=160)
    dname=models.CharField(max_length=160)
    dphone=models.CharField(max_length=150)
    pass1=models.CharField(max_length=150)
    pass2=models.CharField(max_length=150)
    

class Basic(models.Model):
    fac1=models.CharField(max_length=120)
    fac2=models.CharField(max_length=120)
    fac3=models.CharField(max_length=120)
    fac4=models.CharField(max_length=120)
    fac5=models.CharField(max_length=120)

class Ambulance(models.Model):
    city = models.CharField(max_length=120)
    name = models.CharField(max_length=50,default = '0')
    fac1=models.CharField(max_length=120,default = '0')
    fac2=models.CharField(max_length=120,default = '0')
    fac3=models.CharField(max_length=120,default = '0')
    fac4=models.CharField(max_length=120,default = '0')