from rest_framework import serializers
from .models import Inventory
from cafeteria.Items.serializer import ItemSerializer

class InventorySerializer(serializers.ModelSerializer):
    inventory_item_id=ItemSerializer(read_only=True)
    class Meta:
        model = Inventory
        fields = '__all__'
