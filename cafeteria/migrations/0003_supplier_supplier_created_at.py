# Generated by Django 4.0.1 on 2022-04-07 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0002_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_created_at',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]