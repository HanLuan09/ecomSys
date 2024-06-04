from django.contrib.auth.models import AbstractUser
from django.db import models

class Manager(AbstractUser):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.username
