from django.shortcuts import render
from numpy import average
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
            "sales":Order.objects.filter(order_status='Completed').select_related('customer_id').order_by("-id")
        })


def salesReturn(request):
    if request.method == "POST":
        if request.POST.get("btn-salesReturn"):
            print("salesReturn",request.POST.get("sale-return-id"))
            order = Order.objects.get(id=request.POST.get("sale-return-id"))
            if order.customer_id:
                CafeteriaCustomer.objects.filter(id=order.customer_id.id).update(
                    customer_dues=order.customer_id.customer_dues-order.order_total_price
                )
            order.order_status = "Returned"
            order.save()
            return HttpResponseRedirect(reverse("salesReturn"))

    else:
        return render(
            request, "salesReturn.html",{
                "salesReturn":Order.objects.filter(order_status='Returned').select_related('customer_id').order_by("-id")
                }
            )



@api_view(['GET'])
def GetsalesApi(request,pk):
    if request.method == "GET":
        sales = Order.objects.filter(order_status='Completed').filter(id=pk).select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesInvoiceIDsearchApi(request,pk):
    if request.method == "GET":
        sales = Order.objects.filter(order_status='Completed').filter(id=pk).select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesCustomerSearchApi(request):
    if request.method == "GET":
        name=request.GET.get("customer_name")
        print(name,'namem')
        sales = Order.objects.filter(order_status='Completed').filter(customer_id__customer_name__icontains=name).select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})


# salesReturn 
@api_view(['GET'])
def GetsalesReturnApi(request,pk):
    if request.method == "GET":
        sales = Order.objects.filter(id=pk).filter(order_status='Returned').select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesReturnInvoiceIDsearchApi(request,pk):
    if request.method == "GET":
        sales = Order.objects.filter(id=pk).filter(order_status='Returned').select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})

@api_view(['GET'])
def GetsalesReturnCustomerSearchApi(request):
    if request.method == "GET":
        name=request.GET.get("customer_name")
        print(name,'namem')
        sales = Order.objects.filter(order_status='Returned').filter(customer_id__customer_name__icontains=name).select_related('customer_id').order_by("-id")
        if sales:
            serializer = OrderSerializer(sales, many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No sales found"})
