# Generated by Django 3.2.9 on 2021-11-16 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0009_monthlyaudit_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='descripcion',
            new_name='description',
        ),
    ]