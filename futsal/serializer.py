from dataclasses import field
from rest_framework import serializers
from .models import Team, Booking, Match

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields='__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields='__all__'