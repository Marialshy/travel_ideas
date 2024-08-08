from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    STATUS = (
        ('regular','regular'),
        ('registered','registered'),
        ('moderator', 'moderator')
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField('description', max_length=600, default='', blank=True)

    def __str__(self) -> str:
        return self.username