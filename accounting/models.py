from django.db import models
from datetime import datetime

class RentalData(models.Model):
    Full_name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    cnic_no = models.CharField(max_length=15, null=True)
    reference = models.CharField(max_length=100, null=True)
    shop_no = models.CharField(max_length=20)
    electric_bill = models.CharField(max_length=30, null=True)
    gas_bill = models.CharField(max_length=30, null=True)
    rent_pay_to = models.CharField(max_length=50)
    rent_pay_by = models.CharField(max_length=50)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateField(default=datetime.now)


class rentalPayment(models.Model):
    rent_amount = models.IntegerField()
    payment_mode = models.CharField(max_length=25)
    rent_pay_date = models.DateField()
    rent_duration = models.CharField(max_length=25)
    total_rent = models.IntegerField()
    rent_end_date = models.DateField()
    payment_status = models.CharField(max_length=150)
    payment_created_at = models.DateField(default=datetime.now)
    rental_id = models.ForeignKey(RentalData, on_delete=models.CASCADE, related_name='rental_id')
