from django.shortcuts import render
from .functions import *
from django.urls import  reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# Create your views here.

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