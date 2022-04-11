# Generated by Django 3.2 on 2022-04-08 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('item_unit', models.CharField(max_length=30)),
                ('item_category', models.CharField(max_length=30)),
                ('item_brand', models.CharField(max_length=30)),
                ('item_manufacturer', models.CharField(max_length=30)),
                ('item_selling_price', models.IntegerField()),
                ('item_max_selling_quantity', models.IntegerField()),
                ('item_min_selling_quantity', models.IntegerField()),
                ('item_reorder_level', models.IntegerField()),
                ('item_image', models.ImageField(upload_to='items_images/')),
                ('item_description', models.CharField(max_length=100)),
                ('item_status', models.CharField(max_length=20)),
                ('item_expiry_day', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NonStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonStock_item_code', models.IntegerField()),
                ('nonStock_item_name', models.CharField(max_length=50)),
                ('nonStock_item_unit', models.CharField(max_length=30)),
                ('nonStock_item_category', models.CharField(max_length=30)),
                ('nonStock_item_brand', models.CharField(max_length=30)),
                ('nonStock_item_manufacturer', models.CharField(max_length=30)),
                ('nonStock_item_purchase_price', models.IntegerField(default=0)),
                ('nonStock_item_selling_price', models.IntegerField()),
                ('nonStock_item_max_selling_quantity', models.IntegerField()),
                ('nonStock_item_min_selling_quantity', models.IntegerField()),
                ('nonStock_item_image', models.ImageField(upload_to='items_images/')),
                ('nonStock_item_description', models.CharField(max_length=100)),
                ('nonStock_item_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_unit', models.CharField(max_length=30)),
                ('product_category', models.CharField(max_length=30)),
                ('product_brand', models.CharField(max_length=30)),
                ('product_manufacturer', models.CharField(max_length=30)),
                ('product_selling_price', models.IntegerField()),
                ('product_max_selling_quantity', models.IntegerField()),
                ('product_min_selling_quantity', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='items_images/')),
                ('product_description', models.CharField(max_length=100)),
                ('product_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_unit_price', models.IntegerField()),
                ('inventory_unit_tax', models.IntegerField()),
                ('inventory_purchased_quantity', models.IntegerField()),
                ('inventory_sub_total', models.IntegerField()),
                ('inventory_tax_total', models.IntegerField()),
                ('inventory_item_total', models.IntegerField()),
                ('inventory_reference_number', models.IntegerField()),
                ('inventory_expiry_date', models.DateField()),
                ('inventory_stock_in_shop', models.IntegerField()),
                ('inventory_stock_in_storeroom', models.IntegerField()),
                ('inventory_item_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_code', to='cafeteria.items')),
                ('inventory_item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_name', to='cafeteria.items')),
                ('inventory_item_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item_unit', to='cafeteria.items')),
                ('inventory_unit_net_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_net_price', to='cafeteria.items')),
            ],
        ),
    ]
