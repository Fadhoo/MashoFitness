from django.shortcuts import render
from .models import CafeteriaCustomer
from .functions import *
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# Create your views here.
def customer(request):
    if request.method == "POST":
        if request.POST.get("add-customer-data"):
            addCustomer(request)
            return HttpResponseRedirect(reverse("customer"))
    else:
        return render(request, "customer.html", {'customerData': CafeteriaCustomer.objects.all()})


def updateCustomer(request):
    if request.method== "POST":
        if request.POST.get("update-customer-data"):
            updateCustomerData(request)
            return HttpResponseRedirect(reverse("customer"))
    else:
        return render(request, "updateCustomer.html", {'customerData': CafeteriaCustomer.objects.filter(id=request.GET.get("customer")).first()})