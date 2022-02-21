from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
# from .functions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TeamSerializer


def addTeam(request):
    if request.method=="POST":
        if request.POST.get("add-team"):
            Team.objects.create(team_name=request.POST.get("team-name"),captain_name=request.POST.get("captain-name"),contact_number=request.POST.get("contact-number"),team_attended_by=request.POST.get("team-attended-by")).save()
            return render(request,"addTeam.html",{"TeamRecord":Team.objects.all().order_by("-id")})
    else:
        # code here
        
        return render(request,"addTeam.html",{"TeamRecord":Team.objects.all().order_by("-id")})


















def viewTeam(request):
    return render(request, 'viewTeam.html')


def teamDetails(request):
    return render(request, 'teamDetails.html')

def futsal(request):
    return render(request, 'futsal.html')

def futsalMatch(request):
    return render(request, 'futsalMatch.html')

def matches(request):
    return render(request, 'matches.html')

def updateFutsalMatch(request):
    return render(request,"updateFutsalMatch.html")



































# api work
@api_view(['GET'])
def SearchByFutsalField(request):
    field=request.GET.get("field")
    value=request.GET.get("value")
    try:
        if field=="team_name":
            return Response(TeamSerializer(Team.objects.filter(team_name__icontains=value).order_by('-id'),many=True).data)
        elif field=="captain_name":
            return Response(TeamSerializer(Team.objects.filter(captain_name__icontains=value).order_by('-id'),many=True).data)
        elif field=="contact_number":
            return Response(TeamSerializer(Team.objects.filter(contact_number__icontains=value).order_by('-id'),many=True).data)
    except:
        return Response({"message":"No data found"})




# @api_view(['GET'])
# def deleteExpense(request):
#     # print(request.DELETE.get('delete_array'))
#     try:
#         delete_list=request.GET.getlist('arr[]')
#         if delete_list is not None:
#             for i in delete_list:
#                 print(i)
#                 expensesData.objects.filter(id=int(i)).delete()
#             return Response(expensesSerializer(expensesData.objects.order_by('-id'),many=True).data)
#         else:
#             return Response({"error":str("No data selected")})
#     except Exception as e:
#         print(e)
#         return Response({"error":str(e)})


# @api_view(['GET'])
# def searchByExpenseData(request):
#     try:
#         print(request.GET)
#         resultperpage=request.GET.get('resultperpage',None)
#         searchbytype=request.GET.get('searchbytype',None)
#         if searchbytype!='':
#             if resultperpage!="all":
#                 print("if resultperpage!=all:")
#                 return Response(expensesSerializer(expensesData.objects.order_by('-id').filter(expenses_for=searchbytype)[:int(resultperpage)],many=True).data)

#             else:
#                 print("if resultperpage==all:")
#                 return Response(expensesSerializer(expensesData.objects.order_by('-id').filter(expenses_for=searchbytype),many=True).data)
#         else:
            
#             if resultperpage!="all":
#                 print("if resultperpage!=all:  else if")
#                 return Response(expensesSerializer(expensesData.objects.order_by('-id')[:int(resultperpage)],many=True).data)
#             else:
#                 print("if resultperpage==all: else else")
#                 return Response(expensesSerializer(expensesData.objects.order_by('-id'),many=True).data)
        
#     except Exception as e:
#         return Response({"error":str(e)})



# @api_view(['GET'])
# def searchByExpenseDate(request):
#     try:
#         from_date=request.GET.get('fromdate',None)
#         to_date=request.GET.get('todate',None)
#         if from_date is not None and to_date is not None:
#             return Response(expensesSerializer(expensesData.objects.filter(date__range=[from_date,to_date]).order_by('-id'),many=True).data)
#         else:
#             return Response({"error":str("Please select date")})
#     except Exception as e:
#         return Response({"error":str(e)})

# @api_view(['GET'])
# def searchByExpenseHeadOfAccount(request):
#     try:
#         name=request.GET.get('searchbyname',None)
#         if name is not None:
#             return Response(expensesSerializer(expensesData.objects.filter(account_head__icontains=name).order_by('-id'),many=True).data)
#         else:
#             return Response({"error":str("Please select name")})
#     except Exception as e:
#         return Response({"error":str(e)})

