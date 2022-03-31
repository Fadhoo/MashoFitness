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

def null_check(data):
    if data==None:
        return 0
    else:
        return data

def reports(request):
    return render(request,"reports.html", {
        'gym_expense':expensesData.objects.filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'futsal_expense': expensesData.objects.filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'snooker_expense': expensesData.objects.filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'cafeteria_expense': expensesData.objects.filter(expenses_for='Cafeteria').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'rental_expense': expensesData.objects.filter(expenses_for='Rental').aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'total_expenses': expensesData.objects.aggregate(Sum('paid_amount'))['paid_amount__sum']
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

                        "All_total":null_check(snookerTableIncome.objects.filter(snooker_id__date__range=[from_date,to_date]).select_related("snooker_id").aggregate(Sum('amount'))['amount__sum'])+
                        null_check(Bill.objects.filter(bill_created_at__range=[from_date,to_date]).aggregate(Sum('paid'))['paid__sum'])+
                        null_check(Match.objects.filter(date__range=[from_date,to_date]).aggregate(Sum('fee'))['fee__sum'])
                        
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
    return render(request,"expensesReport.html")