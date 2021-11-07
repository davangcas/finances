import datetime

from django.db import models
from django.contrib.auth.models import User


class IncomeCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=180),

    class Meta:
        verbose_name = "Categoría de Ingresos"
        verbose_name_plural = "Categorias de Ingresos"


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(IncomeCategory, on_delete=models.PROTECT)
    descripcion = models.TextField(verbose_name="Descripción", max_length=1000)
    date_created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    date_buy = models.DateTimeField(verbose_name="Fecha", default=datetime.datetime.now(), blank=True, null=True)

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"