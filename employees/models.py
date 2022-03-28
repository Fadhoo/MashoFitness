from django.db import models


class EmployeeRecord(models.Model):
    employee_name = models.CharField(max_length=20)
    employee_contact = models.CharField(max_length=12)
    employee_image = models.ImageField(upload_to='profile_images/')
    employee_cnic = models.CharField(max_length=15, null=True, blank=True)
    employee_email = models.EmailField('enter you email',null=True, blank=True)
    employee_address = models.CharField(max_length=200, null=True, blank=True)
    employee_gender = models.CharField(max_length=10)
    employee_dob = models.DateField(null=True)
    employee_age = models.IntegerField(null=True)
    employee_blood_group = models.CharField(max_length=10,null=True)
    employee_type = models.CharField(max_length=30)
    employee_pay = models.IntegerField(default=0)
    employee_username = models.CharField(max_length=20, null=True)
    employee_password = models.CharField(max_length=20, null=True)
    employee_status = models.CharField(max_length=20)
    super_user=models.BooleanField(default=False) 



