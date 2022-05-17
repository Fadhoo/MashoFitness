from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .models import *
from .functions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ItemSerializer, NonStockSerializer, InventorySerializer
from django.urls import reverse



def addItem(request):
    if request.method== "POST":
        if request.POST.get("save-button"):
            print("save button save button save button save button ")
            if ItemsAdd(request):
                print("item added success")
                return HttpResponseRedirect(reverse("addItem"))

        if request.POST.get("cancel-button"):
            return HttpResponseRedirect(reverse("addItem"))
        
        if request.POST.get("update-button"):
            print("update update update update update update button")
            UpdateItem(request)
            return HttpResponseRedirect(reverse("addItem"))

    else:
        return render(request, "addItem.html", {'addItems': Items.objects.all()})


def addNonStockItem(request):
    if request.method== "POST":
        if request.POST.get("save-button"):
            print("save button save button save button save button ")
            if addNonStockItems(request):
                print("item added success")
                return HttpResponseRedirect(reverse("addNonStockItem"))

        if request.POST.get("cancel-button"):
           return HttpResponseRedirect(reverse("addNonStockItem"))
        
        if request.POST.get("update-button"):
            print("update update update update update update button")
            updateNonStockItems(request)
            return HttpResponseRedirect(reverse("addNonStockItem"))


    else:
        return render(request, "addNonStockItem.html", {'nonStock': NonStock.objects.all()})


def inventory(request):
    # if request.method=="POST":
    #     if request.POST.get("add-inventory-data"):
    #         print("add inventory data")
    #         # addInventory(request)
    #         # return HttpResponseRedirect(reverse("inventory"))
    # else:
        return render(request, "inventory.html", {'addItems': Items.objects.all()})



def customer(request):
    if request.method == "POST":
        if request.POST.get("add-customer-data"):
            print("add customer data")
            addCustomer(request)
            return HttpResponseRedirect(reverse("customer"))
    else:
        return render(request, "customer.html", {'customerData': Customer.objects.all()})


def updateCustomer(request):
    if request.method== "POST":
        if request.POST.get("update-customer-data"):
            print("update customer data")
            updateCustomerData(request)
            return HttpResponseRedirect(reverse("customer"))
    
    else:
        return render(request, "updateCustomer.html", {'customerData': Customer.objects.filter(id=request.GET.get("customer")).first()})




def pos(request):
    return render(request, "pos.html")


def purchasesReturn(request):
    return render(request, "purchaseReturn.html")


def purchases(request):
    return render(request, "purchases.html")


def sales(request):
    return render(request, "sales.html")


def salesReturn(request):
    return render(request, "salesReturn.html")


def salesTerminal(request):
    return render(request, "salesTerminal.html")


def supplier(request):
    if request.method=="POST":
        if request.POST.get("add-supplier-data"):
            print("add supplier data")
            addSupplier(request)
            return HttpResponseRedirect(reverse("supplier"))
    else:
        return render(request, "supplier.html",
         {'supplierData': Supplier.objects.all()})


def updateSupplier(request):
    if request.method== "POST":
        if request.POST.get("update-supplier-data"):
            print("update supplier data")
            updateSupplierData(request)
            return HttpResponseRedirect(reverse("supplier"))
    
    else:
        return render(request, "updateSupplier.html", {'supplierData': Supplier.objects.filter(id=request.GET.get("supplier")).first()})

def cafeteriaExpenses(request):
    return render(request, "cafeteriaExpenses.html")

def updateCafeteriaExpenses(request):
    return render(request, "updateCafeteriaExpenses.html")

def barcodeLabel(request):
    return render(request, "barcodeLabel.html")

# api work
# api for items searching
@api_view(['GET'])
def SearchByItemField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    print(field,value)
    try:
        if field=="Name":
            return Response(ItemSerializer(Items.objects.filter(
                        item_name__icontains=value).order_by('-id'),
                        many=True).data)
        elif field=="Code":
            return Response(ItemSerializer(Items.objects.filter(
                        item_code__icontains=value).order_by('-id'),
                        many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


# api for non-stock search items
@api_view(['GET'])
def SearchByStockField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    print(field,value)
    try:
        if field=="Name":
            return Response(NonStockSerializer(NonStock.objects.filter(
                        nonStock_item_name__icontains=value).order_by('-id'),
                        many=True).data)
        elif field=="Code":
            return Response(NonStockSerializer(NonStock.objects.filter(
                        nonStock_item_code__icontains=value).order_by('-id'),
                        many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


@api_view(['GET'])
def UpdateItemQueryCall(request):
    value=request.GET.get("id")
    try:
        return Response(ItemSerializer(Items.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})


@api_view(['GET'])
def UpdateNonStockItemQueryCall(request):
    value=request.GET.get("nonStock-id")
    try:
        return Response(NonStockSerializer(NonStock.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})

@api_view(['GET'])
def InventoryQueryCall(request):
    value=request.GET.get("id")
    try:
        return Response(InventorySerializer(Inventory.objects.filter(id=value),many=True).data)
    except Exception as e:
        return Response({"message":"No data found {}".format(e)})