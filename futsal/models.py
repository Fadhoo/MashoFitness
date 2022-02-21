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