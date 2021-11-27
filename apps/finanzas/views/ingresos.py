from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from apps.finanzas.models.ingresos import Income, IncomeCategory
from apps.finanzas.forms.ingresos import IncomeForm, IncomeCategoryFrom
from apps.finanzas.services import get_total_expenses, update_monthly_audit


class IncomeCreateView(CreateView):
    template_name = "finanzas/ingresos/create.html"
    model = Income
    form_class = IncomeForm
    success_url = reverse_lazy('finanzas:ingresos')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            update_monthly_audit(request.user, income.date.month, income.date.year)
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
        incomes = Income.objects.filter(user=self.request.user)
        return incomes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ingresos"
        context['total'] = get_total_expenses(self.request.user)
        context['new_button'] = "Nuevo Ingreso"
        context['new_button_url'] = reverse("finanzas:ingresos_create")
        return context


class IncomeUpdateView(UpdateView):
    model = Income
    template_name = "finanzas/ingresos/update.html"
    form_class = IncomeForm
    success_url = reverse_lazy('finanzas:ingresos')

    def form_valid(self, form):
        self.object = form.save()
        update_monthly_audit(self.request.user, self.object.date.month, self.object.date.year)
        return super().form_valid(form)

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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        update_monthly_audit(request.user, self.object.date.month, self.object.date.year)
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Ingreso"
        return context


class IncomeCategoryList(ListView):
    model = IncomeCategory
    template_name = "finanzas/ingresos/category_list.html"

    def get_queryset(self):
        incomes = IncomeCategory.objects.filter(user=self.request.user)
        return incomes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Categorías de ingresos"
        context['new_button'] = "Nueva Categoría"
        context['new_button_url'] = reverse("finanzas:ingresos_categories_create")
        return context

class IncomeCategoryCreateView(CreateView):
    model = IncomeCategory
    template_name = "finanzas/ingresos/category_create.html"
    success_url = reverse_lazy('finanzas:ingresos_categories')
    form_class = IncomeCategoryFrom
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            context = self.get_context_data(**kwargs)
            context['errors'] = form.errors
            return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nueva Categoría de Ingreso"
        return context
