from django.contrib import admin

from apps.finanzas.models.gastos import ExpenseCategory, Expense
from apps.finanzas.models.ingresos import IncomeCategory, Income
from apps.finanzas.models.balance import Havings, Duty
from apps.finanzas.models.inversiones import FixedTerm


admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(IncomeCategory)
admin.site.register(Income)
admin.site.register(Havings)
admin.site.register(Duty)
admin.site.register(FixedTerm)
