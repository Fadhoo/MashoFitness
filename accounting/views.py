from django.shortcuts import render
from expenses.models import expensesData
from django.db.models import Sum
from .models import RentalData
from django.http import HttpResponseRedirect
from .functions import addRental, updateRental
from django.urls import reverse
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
            updateRental(request)
            return HttpResponseRedirect(reverse('rental'))
    else:
        return render(request, "updateRental.html", {'rentalData':RentalData.objects.filter(id=request.GET.get('rent')).first()})
    # return render(request, "updateRental.html",)

def expensesReport(request):
    return render(request,"expensesReport.html")