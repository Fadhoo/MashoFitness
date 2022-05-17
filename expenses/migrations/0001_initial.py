# Generated by Django 3.2 on 2022-05-17 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='expensesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('account_head', models.CharField(max_length=20)),
                ('paid_amount', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=30)),
                ('expenses_for', models.CharField(max_length=20)),
                ('receipent_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
                ('expense_attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employeerecord')),
            ],
        ),
    ]
