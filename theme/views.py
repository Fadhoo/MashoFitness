
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from theme.functions import fetchUniqueCategoryName
from .models import MembershipCategory, Member, BodyAssesments
from .serializers import MembershipCategorySerializer, MemberSerializer,PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .functions import *
from django.db.models import Sum

def fetchAllData(dbmodel):
    data=dbmodel.objects.all()
    ls=[]
    for i in data:
        ls.append(i)
    return ls

def index(request):
    return render(request, 'index.html')






def viewRecord(request):
    return render(request, 'viewRecord.html')




def bodyAssesments(request):
    print("requset data **** ", request.method)
    if request.method == "POST":
        if request.POST.get("add-button"):
            print(Member.objects.filter(id=request.POST.get("member_id")))
            items_add = BodyAssesments.objects.create(neck=request.POST.get("neck"),
                        shoulder=request.POST.get("shoulder"), chest_extended=request.POST.get("chest-extended"),
                        chest_normal=request.POST.get("chest-normal"), forearms=request.POST.get("forearms"),
                        biceps=request.POST.get("biceps"), wrist=request.POST.get("wrist"),
                        upper_abs=request.POST.get("upper-abs"), lower_abs=request.POST.get("lower-abs"),
                        waist=request.POST.get("waist"), hip=request.POST.get("hip"),
                        thigh=request.POST.get("thigh"), calves=request.POST.get("calves"),
                        ankles=request.POST.get("ankles"), body_fat=request.POST.get("body-fat"),
                        vascular=request.POST.get("vascular"), medical_issue=request.POST.get("medical-issue"),
                        body_target=request.POST.get("body-target"), assesment_date=request.POST.get("assesment-date"),
                        member_id=Member.objects.filter(id=request.POST.get("member_id"))[0])
        print("items data ********  ",items_add)
        items_add.save()
        return render(request, 'bodyAssesments.html',  {'zipdata':Member.objects.raw(f'select * from theme_member JOIN theme_bodyassesments on theme_member.id=theme_bodyassesments.member_id_id where theme_bodyassesments.member_id_id={request.POST.get("member_id")};'),
        "all_data":Member.objects.filter(id=request.POST.get('member_id')[0])
        })

    else:
        if request.GET.get("data"):
            print(Member.objects.filter(id=request.GET.get('data')))
            return render(request, "bodyAssesments.html", {"all_data": Member.objects.all().filter(id=request.GET.get('data'))[0],
                                    'zipdata': Member.objects.raw(f'select * from theme_member JOIN theme_bodyassesments on theme_member.id=theme_bodyassesments.member_id_id where theme_bodyassesments.member_id_id={request.GET.get("data")};'), })
        else:
            return render(request, 'viewMembers.html',{
            'zipdata':Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")
            })






def smshistory(request):
    return render(request, 'smshistory.html')

# def reports(request):
#     return render(request,"reports.html")

def printform(request):
    return render(request,"printform.html")

def memberDetails(request):
    if request.method == "POST":
        # if request.POST.get("body-assesment"):
        #     print(request.POST.get("body-assesment"))
        #     return render(request, "bodyAssesments.html", {'zipdata':Member.objects.all().select_related('member_id'),})

        if request.POST.get("edit-member"):
            
        # print(Member.objects.all().filter(id=cid).select_related("membershp_id")[0])
            return render(request,"memberDetails.html",
            {'all_data': Member.objects.all().filter(id=request.POST.get("cid")).select_related("member_membership_id")[0]
            })
        
        if request.POST.get("update-button"):
                print("**************************")
                print(request.POST.get("cid"))
                data = Member.objects.all().filter(id=request.POST.get("cid")).update(member_name=request.POST.get("name"), 
                                    member_father_name=request.POST.get("father_name"), 
                                    member_cnic=request.POST.get("cnic"), 
                                    member_occupation=request.POST.get("occupation"), 
                                    member_gender=request.POST.get("gender"), 
                                    member_address=request.POST.get("address"),
                                    member_contact=request.POST.get("contact"), 
                                    member_emergency_contact=request.POST.get("alternative-number"),
                                    member_dob=request.POST.get("dob"), 
                                    member_age=request.POST.get("age"), 
                                    member_blood_group=request.POST.get("blood_group"), 
                                    # category=request.POST.get("category"), 
                                    member_target=request.POST.get("target"), )
                                    # expiry_date=request.POST.get("expiry")
                print(data)
                return render(request, "viewMembers.html", {'zipdata':Member.objects.all().select_related('member_membership_id').select_related('active_fee_id').order_by('-id') ,})
        if request.POST.get("pay-installment"):
            m_id=request.POST.get("cid")
            payment=Payment.objects.filter(member_id=Member.objects.filter(id=m_id))[0]
    else:
        print("memberDetails",request.GET.get('data'))
        member=Member.objects.all().filter(id=request.GET.get('data')).select_related("member_membership_id").select_related("active_fee_id")[0]
        payment=Payment.objects.filter(fee_id=member.active_fee_id).aggregate(Sum('payment_amount'))
        
        return render(request,"memberDetails.html",
            {'all_data': member,
            "payment":payment['payment_amount__sum']
            })
            

def login(request):
    return render(request,"login.html")

# def income(request):
#     return render(request,"income.html")

def gymSetting(request):
    if request.method == "POST":
        print("post accepted")
        if request.POST.get("addcategory"):
            category = request.POST.get("membershipcategory")
            duration = request.POST.get("membershipduration")
            fee = request.POST.get("membershipfee")
            gender = request.POST.get("membershipgender") 
            add_date = MembershipCategory.objects.create(category_name=category ,category_class=request.POST.get("membership-class"), category_months=duration, category_fee=fee, category_gender=gender)
            add_date.save()
            return render(request, "GymSetting/gymSetting.html",
            {
                'all_data': fetchAllData(MembershipCategory)
            })
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
        "zipdata":Member.objects.all().select_related('member_membership_id')
        # 'zipdata':Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;"),
    })



def addMember(request):
    if request.method=="POST":
        print("post called add member")
        if request.POST.get("addmembersubmit"):
            try:
                if request.POST.get("paidamount") and request.POST.get("remainingamount"):
                    addMemberRecord(request,False)
                    # join=Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")

                    return render(request,"addMember.html", 
                    {
                        'category':fetchUniqueCategoryName(MembershipCategory),
                        'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
                    })                 

                else:
                    addMemberRecord(request,True)
                    # join=Member.objects.raw("SELECT * from theme_member JOIN theme_membershipcategory on theme_member.member_membership_id_id=theme_membershipcategory.id join theme_payment on theme_member.id=theme_payment.member_id_id order by theme_member.id DESC;")

                    return render(request,"addMember.html", 
                    {
                        'category':fetchUniqueCategoryName(MembershipCategory),
                        'zipdata':Member.objects.all().select_related('member_membership_id').order_by('-id'),
                    })

            except Exception as e:
                return HttpResponse(f"error in add member {e}")

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