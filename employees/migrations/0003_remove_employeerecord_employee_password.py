# Generated by Django 4.0.1 on 2022-02-21 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employeerecord_employee_pay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeerecord',
            name='employee_password',
        ),
    ]