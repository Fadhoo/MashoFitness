from django.db import models
from datetime import datetime
# Create your models here.

class Team(models.Model):
    team_name=models.CharField(max_length=25)
    captain_name=models.CharField(max_length=25)
    contact_number=models.IntegerField()
    team_attended_by=models.CharField(max_length=25)
    member_created_at = models.DateField(default=datetime.now())
    member_updated_at = models.DateField(auto_now=True)


class Booking(models.Model):
    time = models.CharField(max_length=25, default="")
    meridiem = models.CharField(max_length=5)
    booking_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)


class Match(models.Model):
    
    date = models.DateField(default=datetime.now())
    fee = models.IntegerField()
    paid= models.CharField(max_length=10, default="Unpaid")
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    booking_time = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_time', default=0)
