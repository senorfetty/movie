from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Account(AbstractUser):
    phone_number= PhoneNumberField()
    groups = models.ManyToManyField(Group, related_name='account_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_set', blank=True)


    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    

class Movie(models.Model):
    title= models.CharField(max_length=100)
    image_url= models.ImageField()
    rating= models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return self.title
    
class  New(models.Model):
    image_url= models.ImageField()

