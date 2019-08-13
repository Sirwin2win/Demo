from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model): 
    name = models.CharField(max_length=50) 
    hotel_Main_Img = models.ImageField(upload_to='images/') 


class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='media')


    def __str__(self):
        return f'{self.user.username}profile'



class Serv(models.Model): 
    name = models.CharField(max_length=50) 
    username=models.CharField(max_length=50)
    code=models.CharField(max_length=50)


class Ever(models.Model): 
    name = models.CharField(max_length=50) 
    username=models.CharField(max_length=50)
    code=models.CharField(max_length=50)

class Teaching(models.Model): 
    username = models.CharField(max_length=50) 
    password=models.CharField(max_length=50)
    code=models.CharField(max_length=50)

class Evangelism(models.Model): 
    username = models.CharField(max_length=50) 
    password=models.CharField(max_length=50)
    code=models.CharField(max_length=50)

class Steward(models.Model): 
    username = models.CharField(max_length=50) 
    password=models.CharField(max_length=50)
    code=models.CharField(max_length=50)