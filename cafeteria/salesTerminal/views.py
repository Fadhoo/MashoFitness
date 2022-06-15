from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from cafeteria.Items.models import Items, NonStock
from cafeteria.Items.serializer import ItemSerializer, NonStockSerializer
from rest_framework.decorators import api_view
from cafeteria.customers.serializer import CustomerSerializer
import json

from cafeteria.customers.models import CafeteriaCustomer
from .functions import *
# Create your views here.

def salesTerminal(request):
    # print("sales terminal")
    # if request.method == "POST":
    #     print("post")
    #     # if request.POST.get("add-item-data"):
    #     print("table data", request.POST.getlist("helloworld[]"))
    #     return HttpResponse(request,"hello")
    # else:
        return render(request, "salesTerminal.html", {
                            "itemsData": Items.objects.all(),
                            "nonStockItems": NonStock.objects.all(),
                            'customer': CafeteriaCustomer.objects.all(),
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

@api_view(['GET'])
def searchbynameCafeteriaCustomer(request):
    customer_name = request.GET.get("searchbyname")
    customer_data = CafeteriaCustomer.objects.filter(customer_name__icontains=customer_name)
    if customer_data:
        return Response(CustomerSerializer(customer_data,many=True).data)
    else:
        return Response(CustomerSerializer(CafeteriaCustomer.objects.all(),many=True).data)


@api_view(['GET'])
def CafeteriaOrderPlacement(request):
    item_name = json.dumps(request.GET)
    item_name=json.loads(item_name)
    for i in item_name:
        for j in json.loads(i)["object"]:
            print(j)
            
    return Response({'message':'success'})