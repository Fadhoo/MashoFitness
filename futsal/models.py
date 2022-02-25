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



class Match(models.Model):
    time = models.DateTimeField(auto_now=True)
    meridiem = models.CharField(max_length=5)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    fee = models.IntegerField()
    paid= models.IntegerField()
    data = models.DateField(auto_now_add=True)

