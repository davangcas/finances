from django.db import models
from django.contrib.auth.models import User


class FixedTerm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)
    days = models.PositiveSmallIntegerField(verbose_name="Días")
    interest_rate = models.DecimalField(verbose_name="Tasa de interés", max_digits=5, decimal_places=2)
    starting_amount = models.DecimalField(verbose_name="Monto Inicial", max_digits=1000, decimal_places=2)
    ending_amount = models.DecimalField(verbose_name="Monto Final", max_digits=1000, decimal_places=2)

    class Meta:
        verbose_name = "Plazo Fijo"
        verbose_name_plural = "Plazos Fijos"

    def __str__(self):
        return "Plazo fijo : Dias - {}, Tasa de Interés - {}, Monto Inicial - ${}, Monto Final - ${}".format(self.days, self.interest_rate, self.starting_amount, self.ending_amount)