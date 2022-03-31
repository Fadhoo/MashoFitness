from django.shortcuts import render
from expenses.models import expensesData
from django.db.models import Sum
from .models import RentalData
from django.http import HttpResponseRedirect
from .functions import addRental, editRental
from django.urls import reverse
from theme.models import Bill
from futsal.models import Match
from snooker.models import snookerTableIncome
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RentalSerializer
from django.contrib import messages
# Create your views here.

def checkNone(data):
    if data == None:
        return 0
    else:
        return data

def reports(request):
    return render(request,"reports.html", {
        # Expenses
        'gym_expense':checkNone(expensesData.objects.filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'futsal_expense': checkNone(expensesData.objects.filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'snooker_expense': checkNone(expensesData.objects.filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'cafeteria_expense': checkNone(expensesData.objects.filter(expenses_for='Cafeteria').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'rental_expense': checkNone(expensesData.objects.filter(expenses_for='Rental').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'total_expenses': checkNone(expensesData.objects.aggregate(Sum('paid_amount'))['paid_amount__sum']),
        # Revenues
        'gym_revenue':checkNone(Bill.objects.aggregate(Sum('paid'))['paid__sum']),
        'futsal_revenue': checkNone(Match.objects.aggregate(Sum('paid'))['paid__sum']),
        'snooker_revenue': checkNone(snookerTableIncome.objects.aggregate(Sum('amount'))['amount__sum']),
        'rental_revenue': checkNone(RentalData.objects.aggregate(Sum('total_rent'))['total_rent__sum']),
        # 'cafeteria_revenue': expensesData.objects.filter(expenses_for='Cafeteria').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'total_revenue': checkNone(Bill.objects.aggregate(Sum('paid'))['paid__sum']) + checkNone(Match.objects.aggregate(Sum('paid'))['paid__sum']) + checkNone(snookerTableIncome.objects.aggregate(Sum('amount'))['amount__sum']) + checkNone(RentalData.objects.aggregate(Sum('total_rent'))['total_rent__sum'])
    })

def rental(request):
    if request.method == 'POST':
        print("post post post post ")
        if request.POST.get('rental-button'):
            print("rental button......")
            addRental(request)
            print(RentalData.objects.all())
            return HttpResponseRedirect(reverse('rental'))
    
    else:
        return render(request, "rental.html", {'rentalData':RentalData.objects.all()})

def revenue(request):
    return render(request, "revenue.html")

def updateRental(request):
    if request.method == 'POST':
        if request.POST.get('update-rental'):
            print("update rental button......")
            editRental(request)
            return HttpResponseRedirect(reverse('rental'))
    else:
        return render(request, "updateRental.html", {'rentalData':RentalData.objects.filter(id=request.GET.get('rent')).first()})
    # return render(request, "updateRental.html",)

def expensesReport(request):
    return render(request,"expensesReport.html")


@api_view(['GET'])
def deleteRentalRecord(request):
    try:
        delete_list=request.GET.getlist('arr[]')
        print(delete_list)
        if delete_list is not None:
            for i in delete_list:
                print(i)
                RentalData.objects.filter(id=int(i)).delete()
            return Response(RentalSerializer(RentalData.objects.all().order_by("-id"),many=True).data)
        else:
            return Response({"error":str("No data selected")})
    except Exception as e:
        print(e)
        return Response({"error":str(e)})

@api_view(['GET'])
def SearchByRentalField(request):
    field=request.GET.get('field')
    value=request.GET.get('value')
    try:
        if field=="Name":
            return Response(RentalSerializer(RentalData.objects.filter(Full_name__icontains=value).order_by('-id'),many=True).data)

        elif field=="Contact":
            return Response(RentalSerializer(RentalData.objects.filter(contact_no__icontains=value).order_by('-id'),many=True).data) 
        
        elif field=="Shop":
            return Response(RentalSerializer(RentalData.objects.filter(shop_no__icontains=value).order_by('-id'),many=True).data)

    except:
        return Response({'message':"No data found"})

@api_view(['GET'])
def searchByRentalDate(request):
    try:
        from_date=request.GET.get('fromdate',None)
        to_date=request.GET.get('todate',None)
        if from_date is not None and to_date is not None:
            return Response(RentalSerializer(RentalData.objects.filter(created_at__range=[from_date,to_date]).order_by('-id'),many=True).data)
    except:
        return Response({'message':"No data found"})