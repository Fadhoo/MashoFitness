from django.shortcuts import render
from expenses.models import expensesData
from django.db.models import Sum
# Create your views here.
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
    return render(request, "rental.html")

def revenue(request):
    return render(request, "revenue.html")

def updateRental(request):
    return render(request, "updateRental.html")

def expensesReport(request):
    return render(request,"expensesReport.html")