
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .functions import CreateAdminUserFirst,addEmployee
from django.shortcuts import render
from django.contrib import messages
from futsal.models import Match, Team
from snooker.models import snookerTableIncome
from django.db.models import Sum
from django.utils import timezone
from expenses.models import  expensesData
import datetime as dt
from theme.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
# def fetchAllData(dbmodel):
#     data=dbmodel.objects.all()
#     ls=[]
#     for i in data:
#         ls.append(i)
#     return ls

User_credentials={}
def index(request):
    global User_credentials
    print(User_credentials)
    if bool(User_credentials):
        if User_credentials['super_user']==True:
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
                'employee':EmployeeRecord.objects.filter(id=User_credentials['id']).first(),
            })
        elif User_credentials['super_user']==False:
            print("employee user")
            return render(request, 'index.html',
            {
                'employee':EmployeeRecord.objects.filter(id=User_credentials['id']).first()}
            )
            
    else:
        return render(request, 'login.html')

def Userlogin(request):
        global User_credentials
        if request.method=="POST":
            try:
                if request.POST.get('login-button'):
                    print("login button ********")
                    username=request.POST.get('user-name')
                    password=request.POST.get('password')
                    
                    if User.objects.get(username=username):
                        user=User.objects.get(username=username)
                        auth=authenticate(username=user.username,password=password)
                        if auth:
                            login(request,auth)
                        print(user.check_password(password))
                        User_credentials['username']=user.username
                        User_credentials['password']=user.password
                        User_credentials['id']=user.id
                        User_credentials['super_user']=user.is_superuser
                        return index(request)
                    else:
                        print("user login failed")
                        messages.error(request,"Invalid username or password")
                        return HttpResponseRedirect(reverse('login'))
            except Exception as e:
                print("login error ",e)
                return HttpResponseRedirect(reverse('login'))
        else:
            CreateAdminUserFirst()
            return render(request, 'login.html')

def employee(request):
    if request.method == "POST":
        print("post **&*&*&*&*&*&*&*&*&*&*&*& ")
        if request.POST.get('add-employee'):
            print("added employee button ********* ")
            addEmployee(request)
            return HttpResponseRedirect(reverse('employee'))
    else:

        return render(request, 'employee.html', {
            'employee':EmployeeRecord.objects.filter(id=User_credentials['id']).first(),
            'employees': EmployeeRecord.objects.all().order_by("-id")}
            )


def logout(request):
    global User_credentials
    User_credentials={}
    return render(request,"login.html")


