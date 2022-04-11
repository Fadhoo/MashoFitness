# Generated by Django 4.0.1 on 2022-04-07 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0003_supplier_supplier_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_account', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_contact', models.IntegerField()),
                ('customer_email', models.CharField(max_length=50)),
                ('customer_status', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_city', models.CharField(max_length=50)),
                ('customer_country', models.CharField(max_length=50)),
                ('customer_created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]