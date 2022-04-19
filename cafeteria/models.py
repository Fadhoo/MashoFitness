from django.db import models
from datetime import datetime




class Items(models.Model):
    item_code = models.CharField(max_length=10)
    item_name = models.CharField(max_length=50)
    item_unit = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_brand = models.CharField(max_length=30, null=True, default="")
    item_manufacturer = models.CharField(max_length=30, null=True, default="")
    item_selling_price = models.IntegerField()
    item_max_selling_quantity = models.IntegerField()
    item_min_selling_quantity = models.IntegerField()
    item_reorder_level = models.IntegerField()
    item_image = models.ImageField(upload_to='items_images/', null=True)
    item_description= models.CharField(max_length=100, null=True, default='')
    item_status = models.CharField(max_length=20, default='Active', null=True)
    item_expiry_day = models.IntegerField()



# class Product(models.Model):
#     product_code = models.CharField(max_length=10)
#     product_name = models.CharField(max_length=50)
#     product_unit = models.CharField(max_length=30)
#     product_category = models.CharField(max_length=30)
#     product_brand = models.CharField(max_length=30)
#     product_manufacturer = models.CharField(max_length=30)
#     product_selling_price = models.IntegerField()
#     product_max_selling_quantity = models.IntegerField()
#     product_min_selling_quantity = models.IntegerField()
#     product_image = models.ImageField(upload_to='items_images/')
#     product_description= models.CharField(max_length=100)
#     product_status = models.CharField(max_length=20)


class NonStock(models.Model):

    nonStock_item_code = models.CharField(max_length=15, default='')
    nonStock_item_name = models.CharField(max_length=50)
    nonStock_item_unit = models.CharField(max_length=30)
    nonStock_item_category = models.CharField(max_length=30)
    nonStock_item_brand = models.CharField(max_length=30, null=True, default="")
    nonStock_item_manufacturer = models.CharField(max_length=30, null=True, default="")
    nonStock_item_purchase_price = models.IntegerField(default=0)
    nonStock_item_selling_price = models.IntegerField()
    nonStock_item_max_selling_quantity = models.IntegerField()
    nonStock_item_min_selling_quantity = models.IntegerField()
    nonStock_item_image = models.ImageField(upload_to='items_images/', null=True)
    # nonStock_item_expire_date = models.DateField()
    nonStock_item_description= models.CharField(max_length=200, null=True, default="")
    nonStock_item_status = models.CharField(max_length=20, null=True, default="")
    

class Inventory(models.Model):
    inventory_unit_price = models.IntegerField()
    inventory_purchased_quantity = models.IntegerField()
    inventory_sub_total = models.IntegerField()
    inventory_tax_total = models.IntegerField()
    inventory_item_total = models.IntegerField()
    inventory_reference_number = models.IntegerField()
    inventory_expiry_date = models.DateField()
    inventory_stock_in_shop = models.IntegerField()
    inventory_stock_in_storeroom = models.IntegerField()

    inventory_item_code = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_item_code")
    inventory_item_name = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_item_name")
    inventory_item_unit = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_item_unit")
    inventory_unit_net_price = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_net_price")
    # inventory_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="inventory_supplier")




class Supplier(models.Model):
    supplier_account = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=50)
    supplier_contact = models.IntegerField()
    supplier_email = models.CharField(max_length=50, null=True, default="")
    supplier_status = models.CharField(max_length=20, null=True, default="")
    supplier_address = models.CharField(max_length=200, null=True, default="")
    supplier_city = models.CharField(max_length=50)
    supplier_country = models.CharField(max_length=50)
    supplier_created_at = models.DateField(default=datetime.now)


class Customer(models.Model):
    customer_account = models.CharField(max_length=50, null=True, default="")
    customer_name = models.CharField(max_length=50)
    customer_contact = models.IntegerField()
    customer_email = models.CharField(max_length=50, null=True, default="")
    customer_status = models.CharField(max_length=20, null=True, default="")
    customer_address = models.CharField(max_length=200, null=True, default="")
    customer_city = models.CharField(max_length=50)
    customer_country = models.CharField(max_length=50)
    customer_created_at = models.DateField(default=datetime.now)