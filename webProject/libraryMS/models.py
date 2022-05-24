from django.db import models
from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.utils.timezone import datetime
from datetime import datetime  
from datetime import timedelta
import uuid

# Create your models here.

#User._meta.get_field('email')._unique = True



class User(AbstractUser):
    is_library_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    password1 = models.CharField(max_length=30, default='') #help_text=password_validation.password_validators_help_text_html
    password2 = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='Images/users', null=True, blank=True)
    

    AbstractUser._meta.get_field('email')._unique = True
    AbstractUser.REQUIRED_FIELDS = ['username', 'password']
    AbstractUser.USERNAME_FIELD = 'email'



class Library_admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, primary_key = True)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        email = self.user.email
        return email




class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, primary_key = True)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        email = self.user.email
        return email
    



