import datetime

from django.views.generic import TemplateView

from apps.finanzas.services import get_dollar_price, update_monthly_audit
from apps.finanzas.models.ingresos import Income
from apps.finanzas.models.balance import MonthlyAudit


class IndexView(TemplateView):
    template_name = "finanzas/index.html"

    def dispatch(self, request, *args, **kwargs):
        update_monthly_audit(request.user)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Inicio"
        context['blue_dollar'] = get_dollar_price()
        context['ultimo_sueldo'] = Income.objects.filter(category__name="Sueldo").last().amount
        context['month_data'] = MonthlyAudit.objects.last()
        return context