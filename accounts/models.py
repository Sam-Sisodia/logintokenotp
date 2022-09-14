
from operator import mod
from posixpath import basename
from pyexpat import model
from django.db import models

# Create your models here.

#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    otp = models.IntegerField(null=True,blank=True)
    #is_verified = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=False)

class StudentDetails(models.Model):
    first_name = models.CharField(max_length= 20,blank= True )
    last_name = models.CharField(max_length= 20,blank= True )
    contact_no  = models.IntegerField(default=False)
