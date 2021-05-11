from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLES = [
        ("1", 'Administrador'),
        ("2", 'Visualizador'),
    ]

    # attributes
    rol = models.CharField(max_length=2, choices=ROLES, default="1")
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username.lower()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)



