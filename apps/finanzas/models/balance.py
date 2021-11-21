from django.db import models
from django.contrib.auth.models import User


class Havings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=150)
    description = models.TextField(verbose_name="Descripción", max_length=1000)
    value = models.DecimalField(verbose_name="Valor del activo", max_digits=500, decimal_places=2)

    class Meta:
        verbose_name = "Activo"
        verbose_name_plural = "Activos"

    def __str__(self):
        return "Usuario : {}, nombre del activo : {}, valor : ${}".format(self.user.username, self.name, self.value)


class Duty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nombre", max_length=150)
    description = models.TextField(verbose_name="Descripción", max_length=1000)
    value = models.DecimalField(verbose_name="Valor del pasivo", max_digits=500, decimal_places=2)

    class Meta:
        verbose_name = "Pasivo"
        verbose_name_plural = "Pasivos"

    def __str__(self):
        return "Usuario : {}, nombre del pasivo : {}, valor : ${}".format(self.user.username, self.name, self.value)


class MonthlyAudit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.DateField(verbose_name="Periodo", blank=True, null=True)
    total_expense = models.DecimalField(verbose_name="Gastos totales", max_digits=1000, decimal_places=2, blank=True, null=True)
    total_income = models.DecimalField(verbose_name="Ingresos totales", max_digits=1000, decimal_places=2, blank=True, null=True)
    monthly_balance = models.DecimalField(verbose_name="Balance Mensual", max_digits=1000, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Auditoria Mensual"
        verbose_name_plural = "Auditoria Mensual"

    def __str__(self):
        return "Periodo : {}, Balance Mensual : $ {}".format(self.period, self.monthly_balance)
