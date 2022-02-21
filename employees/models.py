from django.db import models


class EmployeeRecord(models.Model):
    employee_name = models.CharField(max_length=20)
    employee_contact = models.IntegerField()
    employee_image = models.ImageField(upload_to='profile_images/')
    employee_cnic = models.IntegerField()
    employee_email = models.EmailField('enter you email')
    employee_address = models.CharField(max_length=200)
    employee_gender = models.CharField(max_length=10)
    employee_dob = models.DateField(null=True)
    employee_age = models.IntegerField()
    employee_blood_group = models.CharField(max_length=10)
    employee_type = models.CharField(max_length=30)
    employee_pay = models.IntegerField(default=0)
    employee_username = models.CharField(max_length=20)
    employee_password = models.CharField(max_length=20, default='0000')
    employee_status = models.CharField(max_length=20) 



