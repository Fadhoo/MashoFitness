from django.shortcuts import render
from cafeteria.Items.models import Items
from .models import Inventory
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import InventorySerializer
from django.urls import reverse

# Create your views here.
def inventory(request):
    # if request.method=="POST":
    #     if request.POST.get("add-inventory-data"):
    #         print("add inventory data")
    #         # addInventory(request)
    #         # return HttpResponseRedirect(reverse("inventory"))
    # else:
        return render(request, "inventory.html", {'addItems': Items.objects.all()})

def purchaseReturn(request):
    return render(request, "purchaseReturn.html")


def purchases(request):
    return render(request, "purchases.html")










@api_view(['GET'])
def InventoryQueryCall(request):
    value=request.GET.get("id")
    try:
        return Response(InventorySerializer(Inventory.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})