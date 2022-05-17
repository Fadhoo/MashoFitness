from django.db import models
from cafeteria.Items.models import Items


# Create your models here.
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

    inventory_item_id = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_item_id")