from django.shortcuts import render
from .models import *
from .functions import *


# def fetchAllData(dbmodel):
#     data=dbmodel.objects.all()
#     ls=[]
#     for i in data:
#         ls.append(i)
#     return ls



def employee(request):
    if request.method == "POST":
        print("post **&*&*&*&*&*&*&*&*&*&*&*& ")
        if request.POST.get('add-employee'):
            print("added employee button ********* ")
            addEmployee(request)
            return render(request, 'employee.html', {'employees': EmployeeRecord.objects.all().order_by("-id")})
    else:

        return render(request, 'employee.html', {'employees': EmployeeRecord.objects.all().order_by("-id")})


def createUser(request):
    return render(request,"creteUser.html")
