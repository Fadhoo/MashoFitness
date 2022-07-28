from django.shortcuts import render
from numpy import average
from cafeteria.sales.models import Sales, SalesReturn
from cafeteria.sales.serializer import SalesReturnSerializer, SalesSerializer
from cafeteria.salesTerminal.models import Order, OrderHistory
from django.urls import reverse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cafeteria.salesTerminal.serializer import OrderSerializer
from cafeteria.customers.models import CafeteriaCustomer
# Create your views here.


def sales(request):
    if request.method == "POST":
        # return render(request, "sales.html")
        pass
    else:
        return render(request, "sales.html",{
            "sales":Sales.objects.all().select_related('order_id').order_by("-id")
        })


def salesReturn(request):
    if request.method == "POST":
        if request.POST.get("btn-salesReturn"):
            print("salesReturn",request.POST.get("sale-return-id"))
            sale = Sales.objects.get(id=request.POST.get("sale-return-id"))
            if sale.order_id.customer_id:
                CafeteriaCustomer.objects.filter(id=sale.order_id.customer_id.id).update(
                    customer_dues=sale.order_id.customer_id.customer_dues-sale.order_id.order_total_price
                )
            order=Order.objects.get(id=sale.order_id.id)
            order.order_status="Returned"
            order.save()
            Sales.objects.filter(id=sale.id).get().delete()
            SalesReturn.objects.create(
                order_id=order
            )
            # order.save()
            return HttpResponseRedirect(reverse("salesReturn"))

    else:
        return render(
            request, "salesReturn.html",{
                "salesReturn":SalesReturn.objects.all().select_related('order_id').order_by("-id")
                }
            )



@api_view(['GET'])
def GetsalesApi(request,pk):
    if request.method == "GET":
        sales = Sales.objects.filter(id=pk).order_by("-id")
        if sales:
            serializer = SalesSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesInvoiceIDsearchApi(request,pk):
    if request.method == "GET":
        sales = Sales.objects.filter(id=pk).select_related('order_id').order_by("-id")
        if sales:
            serializer = SalesSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesCustomerSearchApi(request):
    if request.method == "GET":
        name=request.GET.get("customer_name")
        print(name,'namem')
        sales = Sales.objects.filter(order_id__customer_id__customer_name__icontains=name).select_related('order_id').order_by("-id")
        if sales:
            serializer = SalesSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})


# salesReturn 
@api_view(['GET'])
def GetsalesReturnApi(request,pk):
    if request.method == "GET":
        sales = SalesReturn.objects.filter(order_id__id=pk).select_related('order_id').order_by("-id")
        if sales:
            serializer = SalesReturnSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesReturnInvoiceIDsearchApi(request,pk):
    if request.method == "GET":
        sales = SalesReturn.objects.filter(order_id__id=pk).select_related('order_id').order_by("-id")
        if sales:
            serializer = SalesReturnSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesReturnCustomerSearchApi(request):
    if request.method == "GET":
        name=request.GET.get("customer_name")
        print(name,'namem')
        sales = SalesReturn.objects.filter(order_id__customer_id__customer_name__icontains=name).select_related('order_id').order_by("-id")
        if sales:
            serializer = SalesReturnSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})
