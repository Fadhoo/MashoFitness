from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from cafeteria.Items.models import Items, NonStock
from cafeteria.Items.serializer import ItemSerializer, NonStockSerializer
from rest_framework.decorators import api_view

from theme.models import Member
from .functions import *
# Create your views here.

def salesTerminal(request):
    data = Items.objects.all().first()
    return render(request, "salesTerminal.html", {
                            "itemsData": Items.objects.all(),
                            "nonStockItems": NonStock.objects.all(),
                            'customer': Member.objects.all(),
                            })


@api_view(['GET'])
def searchItemInSalesTerminal(request):
    item_name = request.GET.get("item_name")
    item_data = Items.objects.filter(item_name__icontains=item_name)
    nonStock= NonStock.objects.filter(nonStock_item_name__icontains=item_name)
    if item_data and nonStock:
        
        return JsonResponse({"Both":CostomSerializer(item_data,nonStock)})
    elif item_data:
        
        return Response({'Stock':ItemSerializer(item_data,many=True).data})
    elif nonStock:
        
        return Response({"NonStock":NonStockSerializer(nonStock,many=True).data})
    else:
        
        return JsonResponse({"Both":CostomSerializer()})