from django.db import models
import django
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
import os
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django.utils import timezone


phone_validator = RegexValidator(r"^\d{9,10}$", "Enter a valid phone number.")

phone_code_validator = RegexValidator(r"^\+\d{1,3}$")

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_code = models.CharField(
        max_length=4, validators=[phone_code_validator], blank=True, null=True , default= "+254"
    )
    first_name = models.CharField(max_length= 30, blank=True, null= True)
    last_name = models.CharField(max_length = 30, blank= True, null= True)
    username = models.CharField(max_length = 128, unique =True,  default = 'admin')
    password = models.CharField(max_length=128, default='123456')
    phone_number = models.CharField(
        max_length=10, validators=[phone_validator], blank=True, null=True, unique=True)
    
    location = models.CharField(max_length = 128)