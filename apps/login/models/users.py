from django.db import models
from django.contrib.auth.models import User

from apps.login.choices import ROLES


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Rol", max_length=2, choices=ROLES, default="A")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"