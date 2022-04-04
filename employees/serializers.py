from rest_framework import serializers
from .models import EmployeeRecord

class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = '__all__'