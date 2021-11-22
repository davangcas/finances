from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from apps.finanzas.models.gastos import Expense, ExpenseCategory
from apps.finanzas.forms.gastos import ExpenseForm, ExpenseCategoryFrom
from apps.finanzas.services import get_total_expenses


class ExpenseCreateView(CreateView):
    template_name = "finanzas/gastos/create.html"
    model = Expense
    form_class = ExpenseForm
    success_url = reverse_lazy('finanzas:gastos')

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
        context['title'] = "Nuevo Gasto"
        return context


class ExpenseListView(ListView):
    template_name = "finanzas/gastos/list.html"
    model = Expense

    def get_queryset(self):
        expenses = Expense.objects.filter(user=self.request.user)
        return expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Gastos"
        context['total'] = get_total_expenses(self.request.user)
        context['new_button'] = "Nuevo Gasto"
        context['new_button_url'] = reverse("finanzas:gastos_create")
        return context


class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = "finanzas/gastos/update.html"
    form_class = ExpenseForm
    success_url = reverse_lazy('finanzas:gastos')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Gasto"
        return context


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = "finanzas/gastos/delete.html"
    success_url = reverse_lazy('finanzas:gastos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Gasto"
        return context


class ExpenseCategoryList(ListView):
    model = ExpenseCategory
    template_name = "finanzas/gastos/category_list.html"

    def get_queryset(self):
        expenses = ExpenseCategory.objects.filter(user=self.request.user)
        return expenses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Categorías de gastos"
        context['new_button'] = "Nueva Categoría"
        context['new_button_url'] = reverse("finanzas:gastos_categories_create")
        return context


class ExpenseCategoryCreateView(CreateView):
    model = ExpenseCategory
    template_name = "finanzas/gastos/category_create.html"
    success_url = reverse_lazy('finanzas:gastos_categories')
    form_class = ExpenseCategoryFrom
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, user=request.user)
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
        context['title'] = "Nueva Categoría de Gasto"
        return context
