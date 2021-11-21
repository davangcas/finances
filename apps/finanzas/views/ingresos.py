from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.finanzas.models.ingresos import Income
from apps.finanzas.forms.ingresos import IncomeForm
from apps.finanzas.services import get_total_expenses


class IncomeCreateView(CreateView):
    template_name = "finanzas/ingresos/create.html"
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('finanzas:ingresos')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors'] = form.errors
            return render(request, self.template_name, context)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Ingreso"
        return context

class IncomeListView(ListView):
    template_name = "finanzas/ingresos/list.html"
    model = Income

    def get_queryset(self):
        expenses = Income.objects.filter(user=self.request.user)
        return expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ingresos"
        context['total'] = get_total_expenses(self.request.user)
        return context

class IncomeUpdateView(UpdateView):
    model = Income
    template_name = "finanzas/ingresos/update.html"
    form_class = IncomeForm
    success_url = reverse_lazy('finanzas:ingresos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Ingreso"
        return context

class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "finanzas/ingresos/delete.html"
    success_url = reverse_lazy('finanzas:ingresos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Ingreso"
        return context
