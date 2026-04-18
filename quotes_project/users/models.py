from django.db import models
from django.contrib.auth.models import AbstractUser, \
    BaseUserManager
from django.utils.http import strip_tags
 

class CustomUser(AbstractUser):
    first_name
    last_name 
