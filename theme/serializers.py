from rest_framework import serializers
from .models import MembershipCategory, Member,Payment


class MembershipCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipCategory
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
