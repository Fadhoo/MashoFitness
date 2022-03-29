from django.shortcuts import render
from theme.models import *
from snooker.models import *
from employees.models import *
from cafeteria.models import *
from .models import *
from expenses.models import *
from futsal.models import *
from django.db.models import Sum
# Create your views here.
def reports(request):
    if request.method=="POST":
        pass
    else:
        return render(request,"reports.html",
        {
            'gym_revenue':Bill.objects.all().aggregate(Sum('paid'))['paid__sum'],
            'gym_expenses':expensesData.objects.filter(expenses_for="Gym").aggregate(Sum('paid_amount'))['paid_amount__sum'],
        }
        )

def rental(request):
    return render(request, "rental.html")

def revenue(request):
    return render(request, "revenue.html")

def updateRental(request):
    return render(request, "updateRental.html")

def expensesReport(request):
    return render(request,"expensesReport.html")