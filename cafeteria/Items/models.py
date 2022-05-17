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
    item_reorder_level = models.IntegerField()
    item_image = models.ImageField(upload_to='items_images/', null=True)
    item_description= models.CharField(max_length=100, null=True, default='')
    item_status = models.CharField(max_length=20, default='Active', null=True)



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
    nonStock_item_image = models.ImageField(upload_to='items_images/', null=True)
    # nonStock_item_expire_date = models.DateField()
    nonStock_item_description= models.CharField(max_length=200, null=True, default="")
    nonStock_item_status = models.CharField(max_length=20, null=True, default="")
    





