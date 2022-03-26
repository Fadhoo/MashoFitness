
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .functions import *
from django.contrib import messages
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from futsal.models import Match, Team
from snooker.models import snookerTableIncome
from .functions import *
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponseRedirect
from expenses.models import  expensesData
import datetime as dt
from theme.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# def fetchAllData(dbmodel):
#     data=dbmodel.objects.all()
#     ls=[]
#     for i in data:
#         ls.append(i)
#     return ls
def index(request,id=None):
    user=EmployeeRecord.objects.filter(id=id).first()
    if user.super_user==True:
        # user.set_password(user.employee_password)
        # user.save()
        print(user.employee_password)
        print(user.employee_username," is super user")
        # user=authenticate(username=user.employee_username,password=user.employee_password)
        # print("check user ",user)
        # login(request,user)
        print("super user")
        return render(request, 'index.html',
        {
            "total_member":Member.objects.all().count(),
            "total_male":Member.objects.filter(member_gender="Male").count(),
            "total_female":Member.objects.filter(member_gender="Female").count(),
            'member_dues':Fee.objects.filter(status="Unpaid").count(),
            'member_income':Payment.objects.all().aggregate(Sum('payment_amount'))['payment_amount__sum'],
            'member_expense':expensesData.objects.filter(expenses_for='Gym').aggregate(Sum('paid_amount'))['paid_amount__sum'],
            'gym_total_dues':Fee.objects.filter(status="Unpaid").aggregate(Sum('remaining'))['remaining__sum'],
            'futsal_total_team': Team.objects.all().count(),
            'futsal_income':Match.objects.filter(paid="Paid").aggregate(Sum('fee'))['fee__sum'], 
            'futsal_expense': expensesData.objects.filter(expenses_for='Futsal').aggregate(Sum('paid_amount'))['paid_amount__sum'],
            'total_expenses':expensesData.objects.aggregate(Sum('paid_amount'))['paid_amount__sum'],
            'today_snooker_income':snookerTableIncome.objects.select_related('snooker_id').filter(snooker_id__date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(Sum('amount'))['amount__sum'],
            'snooker_expenses':expensesData.objects.filter(expenses_for='Snooker').aggregate(Sum('paid_amount'))['paid_amount__sum'],
            'employee':EmployeeRecord.objects.filter(id=id).first(),
        })
    elif user.super_user==False:
        # user=authenticate(request,username=user.employee_username,password=user.employee_password)
        # login(request,user)
        print("employee user")
        return render(request, 'index.html',
        {
            'employee':EmployeeRecord.objects.filter(id=id).first()}
        )
    else:
        return render(request, 'index.html')

def Userlogin(request):
        if request.method=="POST":
            try:
                if request.POST.get('login-button'):
                    print("login button ********")
                    username=request.POST.get('user-name')
                    password=request.POST.get('password')
                    
                    if EmployeeRecord.objects.filter(employee_username=username,employee_password=password).exists():
                        print("user login success as Admin")
                        messages.success(request,"Login Successful")
                        return index(request,id=EmployeeRecord.objects.filter(employee_username=username,employee_password=password).first().id)
                    else:
                        print("user login failed")
                        messages.error(request,"Login Failed")
                        return HttpResponseRedirect(reverse('login'))
            except Exception as e:
                print("login error ",e)
                return HttpResponseRedirect(reverse('login'))
        else:
            check_admin()
            return render(request, 'login.html')

def employee(request):
    if request.method == "POST":
        print("post **&*&*&*&*&*&*&*&*&*&*&*& ")
        if request.POST.get('add-employee'):
            print("added employee button ********* ")
            addEmployee(request)
            return HttpResponseRedirect(reverse('employee'))
    else:

        return render(request, 'employee.html', {'employees': EmployeeRecord.objects.all().order_by("-id")})


def createUser(request):
    return render(request,"createUser.html")
