from argon2 import PasswordHasher
from django.db import models
from matplotlib.backend_bases import MouseEvent

# Create your models here.
class Crud_opr(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Name