from django.db import models
from django.db import models
from django.utils import timezone
from cafeteria.customers.models import CafeteriaCustomer

class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()
    total = models.FloatField()
    user_id = models.IntegerField()


    def __str__(self):
        return str(self.id)

class SaleReturn(models.Model):
    salesReturn_date = models.DateField(default=timezone.now)
    salesReturn_status = models.CharField(max_length=50, default="Returned")
    salesReturn_total_discount = models.IntegerField(default=0)
    salesReturn_total_price = models.IntegerField(default=0)
    salesReturncustomer_id = models.ForeignKey(CafeteriaCustomer, on_delete=models.CASCADE, related_name="SalesReturncustomer_id", null=True)