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
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import RentalSerializer
from django.contrib import messages


def checkNone(data):
    if data == None:
        return 0
    else:
        return data

def reports(request):
    revenue=checkNone(Bill.objects.aggregate(Sum('paid'))['paid__sum']) + checkNone(Match.objects.aggregate(Sum('paid'))['paid__sum']) + checkNone(snookerTableIncome.objects.aggregate(Sum('amount'))['amount__sum']) + checkNone(RentalData.objects.aggregate(Sum('total_rent'))['total_rent__sum'])
    expense=checkNone(expensesData.objects.aggregate(Sum('paid_amount'))['paid_amount__sum'])
    return render(request,"reports.html", {
        # Expenses
        'gym_expense':checkNone(expensesData.objects.filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'futsal_expense': checkNone(expensesData.objects.filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'snooker_expense': checkNone(expensesData.objects.filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'cafeteria_expense': checkNone(expensesData.objects.filter(expenses_for='Cafeteria').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'rental_expense': checkNone(expensesData.objects.filter(expenses_for='Rental').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'total_expenses': expense,
        # Revenues
        'gym_revenue':checkNone(Bill.objects.aggregate(Sum('paid'))['paid__sum']),
        'futsal_revenue': checkNone(Match.objects.aggregate(Sum('fee'))['fee__sum']),
        'snooker_revenue': checkNone(snookerTableIncome.objects.aggregate(Sum('amount'))['amount__sum']),
        'rental_revenue': checkNone(RentalData.objects.aggregate(Sum('total_rent'))['total_rent__sum']),
        'cafeteria_revenue': checkNone(expensesData.objects.filter(expenses_for='Cafeteria').aggregate(Sum('paid_amount'))['paid_amount__sum']),
        'total_revenue': revenue,
        "profit": revenue-expense,
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
    if request.method=="POST":
        if request.POST.get("revenue-generate"):
            from_date = request.POST.get("from-date")
            to_date = request.POST.get("to-date")
            if request.POST.get("check"):
                value=request.POST.get("check")
                if value=="all-check":
                    print("all check")
                    return render(request,"revenue.html",{
                        'MemberData':Bill.objects.filter(bill_created_at__range=[from_date,to_date]).select_related('member_id').select_related('fee_id'),
                        "gym_revenue_total":Bill.objects.filter(bill_created_at__range=[from_date,to_date]).aggregate(Sum('paid'))['paid__sum'],
                        "futsal_revenue_total":Match.objects.filter(date__range=[from_date,to_date]).aggregate(Sum('fee'))['fee__sum'],
                        "FutsalData":Match.objects.filter(date__range=[from_date,to_date]).select_related('booking_time').select_related('team1').select_related('team2'),
                        "snooker_revenue_total":snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id").aggregate(Sum('amount'))['amount__sum'],
                        "SnookerData":snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id"),

                        "All_total":checkNone(snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id").aggregate(Sum('amount'))['amount__sum'])+
                        checkNone(Bill.objects.filter(bill_created_at__range=[from_date,to_date]).aggregate(Sum('paid'))['paid__sum'])+
                        checkNone(Match.objects.filter(date__range=[from_date,to_date]).aggregate(Sum('fee'))['fee__sum'])
                        
                    })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="gym-check":
                    print("gym check")
                    return render(request, "revenue.html", {'MemberData':Bill.objects.filter(bill_created_at__range=[from_date,to_date]).select_related('member_id').select_related('fee_id'),
                                            "gym_revenue_total":Bill.objects.filter(bill_created_at__range=[from_date,to_date]).aggregate(Sum('paid'))['paid__sum'],
                    })
                elif value=="futsal-check":
                    print("futsal check")
                    return render(request,"revenue.html",{
                        "futsal_revenue_total":Match.objects.filter(date__range=[from_date,to_date]).aggregate(Sum('fee'))['fee__sum'],
                        "FutsalData":Match.objects.filter(date__range=[from_date,to_date]).select_related('booking_time').select_related('team1').select_related('team2'),

                    })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="snooker-check":
                    print("snooker check")
                    return render(request, "revenue.html",
                     {
                        "snooker_revenue_total":snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id").aggregate(Sum('amount'))['amount__sum'],
                        "SnookerData":snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id"),
                     })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="cafeteria-check":
                    print("cafeteria check")
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="rental-check":
                    print("rental check")
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
            else:
                print("no check")
                return render(request, "revenue.html")
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
    if request.method=="POST":
        if request.POST.get("revenue-generate"):
            from_date = request.POST.get("from-date")
            to_date = request.POST.get("to-date")
            if request.POST.get("check"):
                value=request.POST.get("check")
                if value=="all-check":
                    print("all check")
                    return render(request,"expensesReport.html",{
                        "snooker_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum'],
                        "SnookerData":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Snooker'),
                        "futsal_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum'],
                        "FutsalData":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Futsal'),
                        'MemberData':expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Gym'),
                        "gym_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum'],


                        "All_total":checkNone(expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum'])+
                        checkNone(expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum'])+
                        checkNone(expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum'])
                        
                    })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="gym-check":
                    print("gym check")
                    return render(request, "expensesReport.html", {'MemberData':expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Gym'),
                                            "gym_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum'],
                    })
                elif value=="futsal-check":
                    print("futsal check")
                    return render(request,"expensesReport.html",{
                        "futsal_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum'],
                        "FutsalData":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Futsal'),

                    })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="snooker-check":
                    print("snooker check")
                    return render(request, "expensesReport.html",
                     {
                        "snooker_expense_total":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum'],
                        "SnookerData":expensesData.objects.filter(date__range=[from_date,to_date]).filter(expenses_for='Snooker'),
                     })
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="cafeteria-check":
                    print("cafeteria check")
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
                elif value=="rental-check":
                    print("rental check")
                    # return render(request, "revenue.html", {'revenueData':RentalData.objects.filter(rent_date__range=[from_date,to_date])})
            else:
                print("no check")
                return render(request, "expensesReport.html")
    # return render(request, "revenue.html")
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