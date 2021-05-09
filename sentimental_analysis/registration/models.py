from django.db import models
from django.contrib.auth.models import AbstractUser


# customer model
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
