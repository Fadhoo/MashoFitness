from rest_framework import serializers
from .models import snookerIncome,snookerTableIncome

class SnookerIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = snookerIncome
        fields = '__all__'
class snookerTableIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = snookerTableIncome
        fields = '__all__'