# Generated by Django 4.0.1 on 2022-03-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_alter_rentaldata_cnic_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentaldata',
            old_name='rent_end_data',
            new_name='rent_end_date',
        ),
    ]
