from ast import Subscript
from django.db import models
from datetime import datetime

class MembershipCategory(models.Model):
    category_name = models.CharField(max_length=25)
    category_class = models.CharField(max_length=20)
    category_months = models.CharField(max_length=15)
    category_fee = models.IntegerField()
    category_gender=models.CharField(max_length=15)
    category_created_at = models.DateField(default=datetime.now())
    category_updated_at = models.DateField(auto_now=True)



class Member(models.Model):
    member_name = models.CharField(max_length=25)
    member_father_name = models.CharField(max_length=25)
    member_cnic = models.CharField(max_length=13)
    member_contact = models.IntegerField(max_length=11)
    member_emergency_contact = models.IntegerField(max_length=11)
    member_email = models.EmailField()
    member_occupation = models.CharField(max_length=25)
    member_address = models.CharField(max_length=255)
    member_gender = models.CharField(max_length=10)
    member_dob = models.DateField()
    member_age = models.IntegerField()
    member_blood_group = models.CharField(max_length=4)
    member_height = models.CharField(max_length=5)
    member_weight = models.IntegerField()
    member_card_id = models.CharField(max_length=20)
    member_target = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    member_created_at = models.DateField(default=datetime.now())
    member_updated_at = models.DateField(auto_now=True)
    member_membership_start_date = models.DateField()
    member_membership_expiry_date = models.DateField()
    active_fee_id=models.ForeignKey('Fee', on_delete=models.CASCADE, null=True, blank=True,related_name='active_fee')    
    member_membership_id = models.ForeignKey(MembershipCategory, on_delete=models.CASCADE,related_name='member_membership_id')

class Fee(models.Model):
    total=models.IntegerField()
    discount=models.IntegerField()
    payable=models.IntegerField()
    remaining=models.IntegerField()
    status=models.CharField(max_length=10)
    installment=models.BooleanField()
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(auto_now=True)
    member_id=models.ForeignKey(Member,on_delete=models.CASCADE,related_name="member_id")

class Payment(models.Model):
    payment_amount = models.FloatField()
    payment_created_at = models.DateField(default=datetime.now())
    payment_updated_at = models.DateField(auto_now=True)
    fee_id = models.ForeignKey(Fee, on_delete=models.CASCADE,related_name="fee_id")




class BodyAssesments(models.Model):
    neck = models.CharField(max_length=20)
    shoulder = models.CharField(max_length=20)
    chest_extended = models.CharField(max_length=20)
    chest_normal = models.CharField(max_length=20)
    forearms = models.CharField(max_length=20)
    biceps = models.CharField(max_length=20)
    wrist = models.CharField(max_length=20)
    upper_abs = models.CharField(max_length=20)
    lower_abs = models.CharField(max_length=20)
    waist = models.CharField(max_length=20)
    hip = models.CharField(max_length=20)
    thigh = models.CharField(max_length=20)
    calves = models.CharField(max_length=20)
    ankles = models.CharField(max_length=20)
    body_fat = models.CharField(max_length=20)
    vascular = models.CharField(max_length=20)
    medical_issue = models.CharField(max_length=40)
    body_target = models.CharField(max_length=30)
    assesment_date = models.DateTimeField(auto_now_add=True)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    

    

