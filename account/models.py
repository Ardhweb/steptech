from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Choices for the role field
ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('moderator', 'Moderator'),
    ('user', 'User'),
)

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='user',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email