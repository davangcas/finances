import requests
import datetime

from apps.finanzas.models.gastos import Expense
from apps.finanzas.models.balance import MonthlyAudit
from apps.finanzas.models.ingresos import Income


def get_dollar_price():
    url_api = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
    data = requests.get(url_api)
    data = data.json()
    return data['venta']


def get_total_expenses(user):
    expenses = Expense.objects.filter(user=user)
    amount = 0.0

    for expense in expenses:
        amount += float(expense.amount)

    return amount


def update_monthly_audit(user):
    expenses = Expense.objects.filter(user=user)
    incomes = Income.objects.filter(user=user)
    month = datetime.date.today().month
    year = datetime.date.today().year
    expenses = expenses.filter(date__year=year, date__month=month)
    incomes = incomes.filter(date__year=year, date__month=month)
    total_expenses = 0.0
    total_incomes = 0.0

    for expense in expenses:
        total_expenses += float(expense.amount)

    for income in incomes:
        total_incomes += float(income.amount)

    monthly_balance = total_incomes - total_expenses

    monthly_audit = MonthlyAudit.objects.filter(user=user).filter(
        period__year=datetime.date.today().year, 
        period__month=datetime.date.today().month
    )
    monthly_audit = monthly_audit.last()

    if monthly_audit:
        monthly_audit.total_expense = total_expenses
        monthly_audit.total_income = total_incomes
        monthly_audit.monthly_balance = monthly_balance
        monthly_audit.save()
    else:
        new_monthly_audit = MonthlyAudit.objects.create(
            user=user,
            period=datetime.date.today(),
            total_expense=total_expenses,
            total_income=total_incomes,
            monthly_balance=monthly_balance,
        )
        new_monthly_audit.save()


