from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .functions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


def addItem(request):
    if request.method== "POST":
        if request.POST.get("save-button"):
            print("save button save button save button save button ")
            add_item = ItemsAdd(request)
            return render(request, "addItem.html", {'addItems': add_item})

    else:
        return render(request, "addItem.html")


def addNonStockItem(request):
    return render(request, "addNonStockItem.html")


def addProducts(request):
    return render(request, "addProducts.html")


def customer(request):
    return render(request, "customer.html")


def inventory(request):
    return render(request, "inventory.html")


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
    return render(request, "supplier.html")