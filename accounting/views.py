from django.shortcuts import render

# Create your views here.
def income(request):
    return render(request,"income.html")

def reports(request):
    return render(request,"reports.html")