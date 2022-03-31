from rest_framework import serializers
from .models import RentalData

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalData
        fields = '__all__'