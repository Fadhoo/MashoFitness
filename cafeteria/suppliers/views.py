from django.shortcuts import render
from .functions import *
from .models import Supplier
from django.urls import  reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .serializer import SupplierSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

# api work
@api_view(['GET'])
def SearchBySupplierField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    try:
        if field=="name":
            return Response(SupplierSerializer(Supplier.objects.filter(supplier_name__icontains=value).order_by("-id"),many=True).data)
        if field=="email":
            return Response(SupplierSerializer(Supplier.objects.filter(supplier_email__icontains=value).order_by("-id"),many=True).data)
        if field=="number":
            return Response(SupplierSerializer(Supplier.objects.filter(supplier_contact__icontains=value).order_by("-id"),many=True).data)
    except:
        return Response({"message":"No data found"})

@api_view(['GET'])
def deleteSupplier(request):
    try:
        delete_list=request.GET.getlist('arr[]')
        print(delete_list)
        if delete_list is not None:
            for i in delete_list:
                print(i)
                Supplier.objects.filter(id=int(i)).delete()
            return Response(SupplierSerializer(Supplier.objects.all().order_by("-id"),many=True).data)
        else:
            return Response({"error":str("No data selected")})
    except Exception as e:
        print(e)
        return Response({"error":str(e)})