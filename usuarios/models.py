from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    lutador = models.BooleanField(default=False)  # Novo campo

    def __str__(self):
        return self.username
