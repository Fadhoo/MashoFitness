from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from futsal.models import Match, Team
from theme.functions import fetchUniqueCategoryName
from snooker.models import snookerTableIncome
from .models import MembershipCategory, Member, BodyAssesments
from .serializers import MembershipCategorySerializer, MemberSerializer,PaymentSerializer,BillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .functions import *
from django.db.models import Sum
from django.utils import timezone
from django.http import HttpResponseRedirect
from expenses.models import  expensesData

def fetchAllData(dbmodel):
    data=dbmodel.objects.all()
    ls=[]
    for i in data:
        ls.append(i)
    return ls

def index(request):
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
            
    }
    
    )

def login(request):
    return render(request,"login.html")

def viewRecord(request):
    if request.method=="GET":
        bill=Bill.objects.filter(member_id=request.GET.get("cid")).select_related("member_id").select_related("fee_id").select_related("subscription_id").order_by("-id")
        print(bill)
        return render(request, "viewRecord.html", {"member_name":bill[0].member_id.member_name,"memberID":bill[0].member_id.id,
                        'bill': bill,})

def smshistory(request):
    return render(request, 'smshistory.html')

def printform(request):
    return render(request,"printform.html")

def gymSetting(request):
    if request.method == "POST":
        if request.POST.get("addcategory"):
            category = request.POST.get("membershipcategory")
            duration = request.POST.get("membershipduration")
            fee = request.POST.get("membershipfee")
            gender = request.POST.get("membershipgender") 
            add_date = MembershipCategory.objects.create(category_name=category ,category_class=request.POST.get("membership-class"), category_months=duration, category_fee=fee, category_gender=gender)
            add_date.save()
            return HttpResponseRedirect(reverse("gymSetting"))
        if request.POST.get("editcall"):
            form = MembershipCategory.objects.all().filter(id=request.POST.get("cid"))[0]
            return render(request,"GymSetting/editGymSetting.html", {'all_data': form})

    else:
        return render(request,"GymSetting/gymSetting.html", {'all_data': fetchAllData(MembershipCategory)})

def editGymSetting(request):
    if request.method == "POST":
        if request.POST.get("update-category"):
            MembershipCategory.objects.all().filter(id=request.POST.get("cid")).update(
                category_name=request.POST.get("membershipcategory"), category_class=request.POST.get("membership-class"),
                category_months=request.POST.get("membershipduration"),
                category_fee=request.POST.get("membershipfee"), category_gender=request.POST.get("membershipgender"))
            return render(request,"GymSetting/gymSetting.html", {'all_data': fetchAllData(MembershipCategory)})
    else:
        return render(request,"GymSetting/gymSetting.html", {'all_data': fetchAllData(MembershipCategory)})

def gymManagement(request):
    
    return render(request,"gymManagement.html",{
        "zipdata":Member.objects.all().select_related('member_membership_id').order_by("-id")[:10],
        "total_member":Member.objects.all().count(),
        "total_male":Member.objects.filter(member_gender="Male").count(),
        "total_female":Member.objects.filter(member_gender="Female").count(),
        'member_dues':Fee.objects.filter(status="Unpaid").count(),
        'income':Payment.objects.filter(payment_created_at__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(Sum('payment_amount'))['payment_amount__sum'],
        'expense':expensesData.objects.filter(expenses_for='Gym').filter(date__gte=timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)).aggregate(Sum('paid_amount'))['paid_amount__sum'],
        'total_dues':Fee.objects.filter(status="Unpaid").aggregate(Sum('remaining'))['remaining__sum'],
        
        
        # 'zipdata':Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;"),
    })

def memberDetails(request):
    if request.method == "POST":
        if request.POST.get("edit-member"):
            return render(request,"memberDetails.html",
            {'all_data': Member.objects.all().filter(id=request.POST.get("cid")).select_related("member_membership_id")[0]
            })
        
        if request.POST.get("update-button"):
            if request.POST.get("occupation")=="None":
                occupation=None
            else:
                occupation=request.POST.get("occupation")
            if request.POST.get("alternative-number")=="None":
                alternative_number=None
            else:
                alternative_number=request.POST.get("alternative-number")
            data = Member.objects.all().filter(id=request.POST.get("cid")).update(member_name=request.POST.get("name"), 
                member_father_name=request.POST.get("father_name"), 
                member_cnic=request.POST.get("cnic"), 
                member_occupation=occupation, 
                member_gender=request.POST.get("gender"), 
                member_address=request.POST.get("address"),
                member_contact=request.POST.get("contact"), 
                member_emergency_contact=alternative_number,
                member_dob=request.POST.get("dob"), 
                member_age=request.POST.get("age"), 
                member_blood_group=request.POST.get("blood_group"), 
                # category=request.POST.get("category"), 
                member_target=request.POST.get("target"), )
                # expiry_date=request.POST.get("expiry")
            print(data)
            return render(request, "viewMembers.html", {'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id') ,})
        if request.POST.get("pay-installment"):
            if update_payment_installment(request):
                bill=Bill.objects.filter(member_id=request.POST.get("cid")).select_related("member_id").select_related("fee_id").select_related("subscription_id").order_by("-id")
                return render(request, "viewRecord.html", {"member_name":bill[0].member_id.member_name,
                    'bill': bill,})
                # return render(request, "viewMembers.html", {'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id') ,})
            else:
                return HttpResponse(request,"error  in update intallment")
                # return render(request, "viewMembers.html", {'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id') ,})
        if request.POST.get("submit-button"):
            print(request.POST.get("paidamount"))
            print(request.POST.get("remainingamount"))
            if request.POST.get("paidamount") and request.POST.get("remainingamount"):
                renewSubscription(request,False)
                bill=Bill.objects.filter(member_id=request.POST.get("cid")).select_related("member_id").select_related("fee_id").select_related("subscription_id").order_by("-id")
                return render(request, "viewRecord.html", {"member_name":bill[0].member_id.member_name,
                    'bill': bill,})
            else:
                renewSubscription(request,True)
                bill=Bill.objects.filter(member_id=request.POST.get("cid")).select_related("member_id").select_related("fee_id").select_related("subscription_id").order_by("-id")
                return render(request, "viewRecord.html", {"member_name":bill[0].member_id.member_name,
                    'bill': bill,})
    else:
        member=Member.objects.all().filter(id=request.GET.get('data')).select_related("member_membership_id").select_related("active_fee_id")[0]
        payment=Payment.objects.filter(fee_id=member.active_fee_id).aggregate(Sum('payment_amount'))
        
        return render(request,"memberDetails.html",
            {'all_data': member,
            "payment":payment['payment_amount__sum'],
            "category":fetchUniqueCategoryName(MembershipCategory),
            })

def addMember(request):
    if request.method=="POST":
        if request.POST.get("addmembersubmit"):
            try:
                if request.POST.get("paidamount") and request.POST.get("remainingamount"):
                    addMemberRecord(request,False)
                    # join=Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
                    messages.success(request, 'User Added Successful') # Any message you wish
                    # return render(request,"addMember.html", 
                    # {
                    #     'category':fetchUniqueCategoryName(MembershipCategory),
                    #     'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
                    # })    
                    return HttpResponseRedirect(reverse('addMember'))               

                else:
                    addMemberRecord(request,True)
                    # join=Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
                    messages.success(request, 'User Added Successful') # Any message you wish
                    # return render(request,"addMember.html", 
                    # {
                    #     'category':fetchUniqueCategoryName(MembershipCategory),
                    #     'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
                    # })
                    return HttpResponseRedirect(reverse('addMember'))

            except Exception as e:
                    messages.error(request, f'Add member error {e}') # Any message you wish
                    # return render(request,"addMember.html", 
                    # {
                    #     'category':fetchUniqueCategoryName(MembershipCategory),
                    #     'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
                    # })
                    return HttpResponseRedirect(reverse('addMember')) 

        if request.POST.get("edit"):
            form_data = Member.objects.all().filter(id=request.POST.get("id"))[0]
            print(form_data)
            return render(request, "MemberDetails.html", {'update_data': form_data})
      
            
    else:
        # print(Member.objects.all().select_related("membershp_id")[0].payment_status)
        # join=Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
        return render(request, "addMember.html",
             {
                        'category':fetchUniqueCategoryName(MembershipCategory),
                        'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id'),
                    })   

def viewMembers(request):
    if request.method=="POST":
        if request.POST.get("edit-member"):
            # Member.objects.raw(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id where theme_member.id={request.POST.get('cid')} ;")
            return render(request,"memberDetails.html",
            {'all_data': Member.objects.all().filter(id=request.POST.get("cid"))[0]
            })
            # form_data = Member.objects.all().filter(id=request.POST.get("cid"))[0]
            # print(form_data)
            # return render(request, "MemberDetails.html", {'all_data': form_data})
        
    else:
        # Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
        return render(request, 'viewMembers.html',{
            'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
        })

def bodyAssesments(request):
    print("requset data **** ", request.method)
    if request.method == "POST":
        if request.POST.get("add-button"):
            print(Member.objects.filter(id=request.POST.get("member_id")))
            addBodyAssesment(request) 
            return render(request, 'bodyAssesments.html',  {'zipdata':BodyAssesments.objects.filter(member_id=request.POST.get("member_id")).select_related('member_id').order_by('-id'),
            "all_data":Member.objects.filter(id=request.POST.get('member_id'))[0]
            })

    else:
        try:
            if request.GET.get("data"):
                print(Member.objects.filter(id=request.GET.get('data')))
                return render(request, "bodyAssesments.html", {"all_data": Member.objects.all().filter(id=request.GET.get('data'))[0],
                                        'zipdata': BodyAssesments.objects.filter(member_id=request.GET.get("data")).select_related("member_id").order_by("-id"), })
            elif request.GET.get("delete_id"):
                member_id=BodyAssesments.objects.filter(id=request.GET.get("delete_id"))[0].member_id.id
                BodyAssesments.objects.filter(id=request.GET.get("delete_id")).delete()
                print(BodyAssesments.objects.filter(member_id=member_id).select_related("member_id").order_by("-id"))
                return render(request, "bodyAssesments.html", {"all_data": Member.objects.all().filter(id=member_id)[0],
                                        'zipdata': BodyAssesments.objects.filter(member_id=member_id).select_related("member_id").order_by("-id"), })
        except:
            return render(request, "addMember.html",
             {
                        'category':fetchUniqueCategoryName(MembershipCategory),
                        'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id'),
                    })

# """"
# API WORK 
# """

@api_view(['GET'])
def get_membershipCategory(request):
    print(request.method)
    if request.method == "GET":
        category_name=request.query_params.get('category_name',None)
        category_class=request.query_params.get('category_class',None)
        category_gender=request.query_params.get("category_gender",None)
        print(category_class,category_name)
        if category_class is not None and category_class is not None and category_gender is not None:
            try:
                return Response(MembershipCategorySerializer(MembershipCategory.objects.all().filter(category_name=category_name).filter(category_class=category_class).filter(category_gender=category_gender),many=True).data)
            except Exception as e:
                return Response({"error":e})
        

@api_view(['GET'])
def deleteMember(request):
    # print(request.DELETE.get('delete_array'))
    try:
        delete_list=request.GET.getlist('arr[]')
        if delete_list is not None:
            for i in delete_list:
                print(i)
                Member.objects.filter(id=int(i)).delete()
            return Response(MemberSerializer(Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id'),many=True).data)
        else:
            messages.info(request,"No data found")
            return Response({"error":str("No data selected")})
    except Exception as e:
        print(e)
        return Response({"error":str(e)})


@api_view(['GET'])
def searchbydata(request):
    try:
        print(request.GET)
        resultperpage=request.GET.get('resultperpage',None)
        searchbytype=request.GET.get('searchbytype',None)
        print(resultperpage)
        print(type(resultperpage))
        if searchbytype!='':
            if resultperpage!="all":
                print("if resultperpage!=all:")
                # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id where  theme_payment.payment_status='{searchbytype}' order by theme_member.id DESC LIMIT {int(resultperpage)};")
                return Response(MemberSerializer(Member.objects.all().select_related('member_membership_id').select_related("active_fee_id").filter(active_fee_id__status=searchbytype).order_by('-id')[:int(resultperpage)],many=True).data)
            else:
                print("if resultperpage==all:")
                # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id where  theme_payment.payment_status='{searchbytype}' order by theme_member.id DESC;")
                return Response(MemberSerializer(Member.objects.all().select_related('member_membership_id').select_related("active_fee_id").filter(active_fee_id__status=searchbytype).order_by('-id'),many=True).data)
        else:
            if resultperpage!="all":
                print("if resultperpage!=all:  else if")
                # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC LIMIT {int(resultperpage)};")
                return Response(MemberSerializer(Member.objects.all().select_related('member_membership_id').select_related("active_fee_id").order_by('-id')[:int(resultperpage)],many=True).data)
            else:
                print("if resultperpage==all: else else")
                # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
                return Response(MemberSerializer(Member.objects.all().select_related('member_membership_id').select_related("active_fee_id").order_by('-id'),many=True).data)
    except Exception as e:
        return Response({"error":str(e)})


@api_view(['GET'])
def searchbydate(request):
    try:
        from_date=request.GET.get('fromdate',None)
        to_date=request.GET.get('todate',None)
        if from_date is not None and to_date is not None:
            # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id where  theme_member.member_created_at between '{from_date}' and '{to_date}' order by theme_member.id DESC;")
            return Response(MemberSerializer(Member.objects.all().select_related("member_membership_id").select_related("active_fee_id").order_by('-id').filter(member_created_at__range=[from_date,to_date]),many=True).data)
        else:
            return Response({"error":str("Please select date")})
    except Exception as e:
        return Response({"error":str(e)})

@api_view(['GET'])
def searchbyname(request):
    try:
        name=request.GET.get('searchbyname',None)
        if name is not None:
            # CustomizeSerializer(f"SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id where  theme_member.member_name like '%{name}%' order by theme_member.id DESC;")
            return Response(MemberSerializer(Member.objects.all().select_related("member_membership_id").select_related("active_fee_id").order_by('-id').filter(member_name__icontains=name),many=True).data)
        else:
            return Response({"error":str("Please select name")})
    except Exception as e:
        return Response({"error":str(e)})

@api_view(['GET'])
def testing(request):
    try:
        return Response(PaymentSerializer(Payment.objects.all().filter(fee_id__member_id=28),many=True).data)
    except Exception as e:
        return Response({"error":str(e)})

@api_view(['GET'])
def searchBillDate(request):
    try:
        from_date=request.GET.get('fromdate',None)
        to_date=request.GET.get('todate',None)
        id=request.GET.get('id',None)
        if from_date is not None and to_date is not None:
            return Response(BillSerializer(Bill.objects.filter(member_id=id).filter(bill_created_at__range=[from_date,to_date]),many=True).data)
        else:
            return Response({"error":str("Please select date")})
    except Exception as e:
        return Response({"error":str(e)})