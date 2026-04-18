from django.db import models
from django.utils.html import strip_tags
from django.contrib.auth.models import AbstractUser, \
    BaseUserManager
 

class CustomUserManager(BaseUserManager):
    #create simple user whiotout extrafields
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('the emails must be')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    #somethiing like register user like admin with difirrent extra fields
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have "is_staff" = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have "is_staff" = True')

        return self.create_user(email, first_name, last_name, password=None, **extra_fields)


class CustomUser(AbstractUser):
    #our user in db (we using postgresql)
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
    



"""
after creation models we need to setting this custom user
"""