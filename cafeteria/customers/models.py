from django.db import models
from datetime import datetime
# Create your models here.

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