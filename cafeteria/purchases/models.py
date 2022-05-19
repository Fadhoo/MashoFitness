from django.db import models
from cafeteria.Items.models import Items
from cafeteria.suppliers.models import Supplier

# Create your models here.
class Inventory(models.Model):
    inventory_unit_price = models.IntegerField(default=0)
    inventory_net_price = models.IntegerField(default=0)
    inventory_purchased_quantity = models.IntegerField(default=0)
    inventory_sub_total = models.IntegerField(default=0)
    inventory_item_total = models.IntegerField(default=0)
    inventory_order_number = models.IntegerField(default=0)
    inventory_reference_number = models.IntegerField(default=0)
    inventory_stock_in_shop = models.IntegerField(default=0)

    inventory_item_id = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="inventory_item_id")
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="supplier_id", null=True)