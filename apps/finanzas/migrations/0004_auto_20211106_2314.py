# Generated by Django 3.2.9 on 2021-11-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_auto_20211106_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date_buy',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_buy',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
    ]
