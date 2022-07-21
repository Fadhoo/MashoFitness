from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from cafeteria.Items.models import Items, NonStock
from cafeteria.Items.serializer import ItemSerializer, NonStockSerializer
from rest_framework.decorators import api_view
from cafeteria.customers.serializer import CustomerSerializer
import json

from cafeteria.customers.models import CafeteriaCustomer
from .models import Order
from .serializer import OrderHistorySerializer, OrderSerializer
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
                            "itemsData": Inventory.objects.select_related("inventory_item_id").all(),
                            "nonStockItems": NonStock.objects.all(),
                            'customer': CafeteriaCustomer.objects.all(),
                            "orders": Order.objects.all().select_related("customer_id"),
                            "mashoo":CafeteriaCustomer.objects.filter(customer_name="Mashoo").first(),
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
def searchbynameCafeteriaOrder(request):
    customer_name = request.GET.get("searchbyname")

    order_data = Order.objects.filter(customer_id__customer_name__icontains=customer_name)
    if order_data:
        return Response(OrderSerializer(order_data,many=True).data)
    else:
        return Response(OrderSerializer(Order.objects.all(),many=True).data)

@api_view(['GET'])
def orderDetails(request):
    order_id = request.GET.get("id")
    order_data = OrderHistory.objects.filter(order_id__id=order_id)
    if order_data:
        return Response(OrderHistorySerializer(order_data,many=True).data)
    else:
        return Response(OrderHistorySerializer(OrderHistory.objects.all(),many=True).data)

@api_view(['GET'])
def CafeteriaOrderPlacementAdmin(request):
    item_name = json.dumps(request.GET)
    for i in json.loads(item_name):
        obj=json.loads(i)
        c=CafeteriaCustomer.objects.filter(customer_name="Mashoo").first()
        # print(c)
        if c:
            c.customer_dues=c.customer_dues+int(obj["total-price"])
            c.save()
            order=Order.objects.create(order_total_discount=obj["total-discount"],order_total_price=obj["total-price"],customer_id=c)
            for j in obj["object"]:
                OrderPlaced(dict(j),order)
            return Response({'message':'success'})
        else:
            CafeteriaCustomer.objects.create(customer_name="Mashoo",customer_dues=int(obj["total-price"]),customer_contact=232323232323)
            order=Order.objects.create(order_total_discount=obj["total-discount"],order_total_price=obj["total-price"],customer_id=c)
            for j in obj["object"]:
                OrderPlaced(dict(j),order)
            return Response({'message':'success'})
            
@api_view(['GET'])
def CafeteriaOrderPlacement(request):
    item_name = json.dumps(request.GET)
    for i in json.loads(item_name):
        obj=json.loads(i)
        if obj.get("member-id"):
            c=CafeteriaCustomer.objects.filter(id=obj["member-id"]).first()
            c.customer_dues=c.customer_dues+int(obj["total-price"])
            c.save()
            order=Order.objects.create(order_total_discount=obj["total-discount"],order_total_price=obj["total-price"],customer_id=c)
        else:
            order=Order.objects.create(order_total_discount=obj["total-discount"],order_total_price=obj["total-price"])
        for j in obj["object"]:
            OrderPlaced(dict(j),order)
    return Response({'message':'success'})