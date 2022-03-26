from django.shortcuts import render

# Create your views here.
def reports(request):
    return render(request,"reports.html")

def rental(request):
    return render(request, "rental.html")

def revenue(request):
    return render(request, "revenue.html")

def updateRental(request):
    return render(request, "updateRental.html")

def expensesReport(request):
    return render(request,"expensesReport.html")