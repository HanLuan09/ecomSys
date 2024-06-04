from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=False, null=True, default=None)
    password = models.CharField(max_length=255)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
    
class UserAddress(models.Model):
    
    apartment_number = models.IntegerField()
    street = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.address
    
class UserProfile(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

