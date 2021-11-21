from django.urls import path

from apps.finanzas.views.index import IndexView
from apps.finanzas.views.gastos import *
from apps.finanzas.views.ingresos import *

app_name = "finanzas"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("gastos/", ExpenseListView.as_view(), name="gastos"),
    path("gastos/nuevo/", ExpenseCreateView.as_view(), name="gastos_create"),
    path("gastos/editar/<int:pk>/", ExpenseUpdateView.as_view(), name="gastos_update"),
    path("gastos/eliminar/<int:pk>/", ExpenseDeleteView.as_view(), name="gastos_delete"),
    path("ingresos/", IncomeListView.as_view(), name="ingresos"),
    path("ingresos/nuevo/", IncomeCreateView.as_view(), name="ingresos_create"),
    path("ingresos/editar/<int:pk>/", IncomeUpdateView.as_view(), name="ingresos_update"),
    path("ingresos/eliminar/<int:pk>/", IncomeDeleteView.as_view(), name="ingresos_delete"),
]