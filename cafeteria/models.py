from django.db import models




class addItems(models.Model):
    item_code = models.IntegerField()
    item_name = models.CharField(max_length=50)
    item_unit = models.CharField(max_length=30)
    item_category = models.CharField(max_length=30)
    item_brand = models.CharField(max_length=30)
    item_manufacturer = models.CharField(max_length=30)
    item_selling_price = models.IntegerField()
    item_max_selling_quantity = models.IntegerField()
    item_min_selling_quantity = models.IntegerField()
    item_reorder_level = models.IntegerField()
    item_image = models.ImageField(upload_to='items_images/')
    search_tag = models.CharField(max_length=50)
    item_description= models.CharField(max_length=100)
    item_status = models.CharField(max_length=20)
    item_expiry = models.DateField()



class addProduct(models.Model):
    product_code = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_unit = models.CharField(max_length=30)
    product_category = models.CharField(max_length=30)
    product_brand = models.CharField(max_length=30)
    product_manufacturer = models.CharField(max_length=30)
    product_selling_price = models.IntegerField()
    product_max_selling_quantity = models.IntegerField()
    product_min_selling_quantity = models.IntegerField()
    product_reorder_level = models.IntegerField()
    product_image = models.ImageField(upload_to='items_images/')
    product_search_tag = models.CharField(max_length=50)
    product_description= models.CharField(max_length=100)
    product_status = models.CharField(max_length=20)
    product_expiry = models.DateField()