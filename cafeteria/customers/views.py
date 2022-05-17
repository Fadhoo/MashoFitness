from django.shortcuts import render
from .models import Customer
from .functions import *
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
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