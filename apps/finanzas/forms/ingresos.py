import datetime

from django import forms

from apps.finanzas.models.ingresos import Income, IncomeCategory


class IncomeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(
            widget=forms.Select(attrs={
                "class": 'form-control select2',
                "style": "width:100%",
            }),
            label="Categoría",
            required=True,
            queryset=IncomeCategory.objects.filter(user=user).order_by('name'),
            initial=IncomeCategory.objects.filter(user=user).order_by('name').first(),
        )
        self.fields['amount'] = forms.DecimalField(
            widget=forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            label="Monto",
            required=True,
        )
        self.fields['description'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            label="Descripción",
            required=True,
        )
        self.fields['date'] = forms.DateField(
            widget=forms.DateInput(
                attrs={
                    "class": "form-control",
                }
            ),
            label="Fecha",
            required=True,
            initial=datetime.date.today(),
        )

    class Meta:
        model = Income
        fields = ['category', 'amount', 'description', 'date']


class IncomeCategoryFrom(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            label="Nombre",
            required=True,
        )

    class Meta:
        model = IncomeCategory
        fields = ['name',]
