# Generated by Django 3.2 on 2022-03-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snooker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snookerincome',
            name='attened_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='snookertableincome',
            name='minutes_per_table',
            field=models.CharField(max_length=50),
        ),
    ]
