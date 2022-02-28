from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *
from .functions import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TeamSerializer, MatchSerializer, BookingSerializer




def futsal(request):
    return render(request, 'futsal.html',{"TeamRecord":Team.objects.all().order_by("-id")})

def addTeam(request):
    if request.method=="POST":
        if request.POST.get("add-team"):
            Team.objects.create(team_name=request.POST.get("team-name"),captain_name=request.POST.get("captain-name"),contact_number=request.POST.get("contact-number"),team_attended_by=request.POST.get("team-attended-by")).save()
            return render(request,"addTeam.html",{"TeamRecord":Team.objects.all().order_by("-id")})
    else:
        # code here
        if request.POST.get("edit-team"):
            print(request.POST.get("edit-team"))
        return render(request,"addTeam.html",{"TeamRecord":Team.objects.all().order_by("-id")})


def viewTeam(request):
    return render(request, 'viewTeam.html',{"TeamRecord":Team.objects.all().order_by("-id")})

def teamDetails(request):
    if request.method=="POST":
        if request.POST.get("update-team"):
            Team.objects.filter(id=request.POST.get("id")).update(team_name=request.POST.get("team-name"),
                    captain_name=request.POST.get("captain-name"), contact_number=request.POST.get("contact"), team_attended_by=request.POST.get("attended-by"))
            return render(request,"addTeam.html",{"TeamRecord":Team.objects.all().order_by("-id")})
    else:
        if request.GET.get("team-details"):
            team_id=request.GET.get("team-details")
            team_details=Team.objects.filter(id=team_id)[0]
            print(team_details.team_name)
            return render(request,"teamDetails.html",{"TeamRecord":team_details})
        # return render(request, 'teamDetails.html')


def futsalMatch(request):
    if request.method=="POST":
        if request.POST.get("add-match"):
            print("add book add book add book")
            addMatch = addMatchBooking(request)
            if addMatch:
                return render(request, "matches.html", {'TeamRecord': Match.objects.all()})
            else:
                pass
    else:
        if request.GET.get("futsal-match"):
            return render(request,"futsalMatch.html", {"TeamRecord":Team.objects.all().filter(id=request.GET.get("futsal-match"))[0],
            "teamNames": Team.objects.all().exclude(id=request.GET.get("futsal-match"))
            })
        # if request.GET.get("futsal-match"):
        #     match_id=request.GET.get("futsal-match")
        #     futsal_match=FutsalMatch.objects.filter(id=match_id)[0]
        #     print(futsal_match.match_name)
        #     return render(request,"futsalMatch.html",{"FutsalMatch":futsal_match})
        return render(request, 'futsalMatch.html', {'TeamRecord': Match.objects.all()})

def matches(request):
    if request.method == "POST":
        pass
    else:
        if request.GET.get("match_done_row_id"):
            pass
        if request.GET.get("match_edit_row_id"):
            match=Match.objects.filter(id=request.GET.get("match_edit_row_id"))[0]
            return render(request, "updateFutsalMatch.html", {'TeamRecord': match,
            "teamNames": Team.objects.all().exclude(team_name=match.team1.team_name)})
    
    return render(request, 'matches.html', {'TeamRecord': Match.objects.all()})

def updateFutsalMatch(request):
    if request.method == "POST":
        if request.POST.get("update-detail"):
            print("edit edit edit edit **** ")
            update_match = updateMatchBooking(request)
            print(update_match)
            
            

    return render(request,"updateFutsalMatch.html", {"TeamRecord": Match.objects.all()})

























@api_view(["GET"])
def searchByTeamData(request):
    try:
        print(request.GET)
        resultperpage = request.GET.get("result-per-page", None)

        if resultperpage!="All":
            print("result per page is not equal to all")
            return Response(TeamSerializer(Team.objects.order_by('-id')[:int(resultperpage)],many=True).data)

        else:
            return Response(TeamSerializer(Team.objects.order_by('-id'),many=True).data)

    except Exception as e:
        return Response({"error": str(e)})









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




@api_view(['GET'])
def deleteTeamRecord(request):
    # print(request.DELETE.get('delete_array'))
    try:
        delete_list=request.GET.getlist('arr[]')
        print(delete_list)
        if delete_list is not None:
            for i in delete_list:
                print(i)
                Team.objects.filter(id=int(i)).delete()
            return Response(TeamSerializer(Team.objects.all().order_by("-id"),many=True).data)
        else:
            return Response({"error":str("No data selected")})
    except Exception as e:
        print(e)
        return Response({"error":str(e)})

@api_view(['GET'])
def getBookings(request):
    date=request.GET.get('booking_date')
    print(date)
    try:
        return Response(BookingSerializer(createDailyMatchTimeTable(date),many=True).data)
    except Exception as e:
        return Response({"error":str(e)})


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

