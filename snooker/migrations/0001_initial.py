# Generated by Django 3.2 on 2022-04-19 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='snookerIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('snooker_attened_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='snooker_attened_by', to='employees.employeerecord')),
            ],
        ),
        migrations.CreateModel(
            name='snookerTableIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('table_number', models.CharField(max_length=10)),
                ('minutes_per_table', models.CharField(max_length=50)),
                ('snooker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snooker.snookerincome')),
            ],
        ),
    ]
