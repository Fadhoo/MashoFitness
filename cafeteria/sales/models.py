from django.db import models
from cafeteria.Items.models import Items

class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()
    total = models.FloatField()
    user_id = models.IntegerField()


    def __str__(self):
        return str(self.id)
