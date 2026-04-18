from django.db import models
from django.contrib.auth.models import AbstractUser, \
    BaseUserManager
from django.utils.http import strip_tags
 
class CustomUserManager(BaseUserManager):
    pass




class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=70)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address1 = models.CharField(max_length=160, blank=True, null=True)
    address2 = models.CharField(max_length=160, blank=True, null=True)
    city =models.CharField(max_length=160, blank=True, null=True)
    country = models.CharField(max_length=160, blank=True, null=True)
    province = models.CharField(max_length=160, blank=True, null=True)
    postal_code = models.CharField(max_length=160, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    marketing_consent1 = models.BooleanField(default=False)
    marketing_consent2 = models.BooleanField(default=False)

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email