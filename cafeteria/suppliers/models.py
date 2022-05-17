from django.db import models
from datetime import datetime
# Create your models here.

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