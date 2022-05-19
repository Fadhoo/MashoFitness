from django.shortcuts import render
from cafeteria.Items.models import Items
from .models import Inventory
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import InventorySerializer
from django.urls import reverse
from .functions import UpdateInventory

# Create your views here.
def inventory(request):
    if request.method=="POST":
        if request.POST.get("add-inventory-data"):
            print("add inventory data")
            UpdateInventory(request)
            return HttpResponseRedirect(reverse("inventory"))
    else:
        return render(request, "inventory.html", {
                    # 'addItems': Items.objects.all(),
                    'inventoryData': Inventory.objects.all().select_related('inventory_item_id')})  

def purchaseReturn(request):
    return render(request, "purchaseReturn.html")


def purchases(request):
    return render(request, "purchases.html")










@api_view(['GET'])
def updateInventoryQueryCall(request):
    value=request.GET.get("inventory-id")
    print(value)
    try:
        print(Inventory.objects.filter(id=value))
        return Response(InventorySerializer(Inventory.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})