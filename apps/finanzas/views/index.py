import datetime

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from apps.finanzas.services import get_dollar_price
from apps.finanzas.models.balance import MonthlyAudit


class IndexView(TemplateView):
    template_name = "finanzas/index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Inicio"
        context['blue_dollar'] = get_dollar_price()
        context['month_data'] = MonthlyAudit.objects.last()
        return context