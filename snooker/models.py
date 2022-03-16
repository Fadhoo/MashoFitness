from django.db import models


class snookerIncome(models.Model):
    description = models.CharField(max_length=300)
    attened_by = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    

class snookerTableIncome(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    table_number = models.CharField(null=False, blank=False, max_length=10)
    minutes_per_table = models.CharField(max_length=50,null=False, blank=False)
    snooker_id = models.ForeignKey(snookerIncome, on_delete=models.CASCADE)




    
