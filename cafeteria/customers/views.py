from django.shortcuts import render
from .models import Customer
from .functions import *
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CustomerSerializer
# Create your views here.
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

# api work
@api_view(['GET'])
def SearchByCustomerField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    try:
        if field=="name":
            return Response(CustomerSerializer(Customer.objects.filter(customer_name__icontains=value).order_by("-id"),many=True).data)
        if field=="number":
            return Response(CustomerSerializer(Customer.objects.filter(customer_contact__icontains=value).order_by("-id"),many=True).data)
        if field=="status":
            return Response(CustomerSerializer(Customer.objects.filter(customer_status__icontains=value).order_by("-id"),many=True).data)
    except:
        return Response({"message":"No data found"})

# def customerr(request):
#     pass