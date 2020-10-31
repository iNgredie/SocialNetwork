from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class UserNet(AbstractBaseUser):
    """Custom user model"""
    middle_name = models.CharField(max_length=50)
    firs_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)



