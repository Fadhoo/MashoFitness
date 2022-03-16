from datetime import datetime
from .models import snookerIncome,snookerTableIncome
record="""
select s.id, s.description, s.attened_by, s.date , sum(t.amount) as total_income
from snooker_snookerincome s
join snooker_snookertableincome t on s.id=t.snooker_id_id GROUP by t.snooker_id_id
order by s.id desc
"""
def addSnookerIncome():
    try:
        add=snookerIncome.objects.create(
        description="",
        attened_by="",
        date=datetime.now()
        )
        add.save()
        return add
    except Exception as e:
        print("add income error:",e)

def addTableIncome(request,id):
    try:
        print("add table income")
        add=snookerTableIncome.objects.create(
        amount=request.POST.get("amount"),
        table_number=request.POST.get("table-number"),
        minutes_per_table=request.POST.get("minutes-per-table"),
        snooker_id=id
        )
        add.save()
        print("add table income success")
        return True
    except Exception as e:
        print("add table income error:",e)
        return False
        
def updateSnookerIncome(request,obj):
    try:
        if request.POST.get("description"):
            des=request.POST.get("description")
        else:
            des=''
        snookerIncome.objects.filter(id=obj.id).update(
        description=des,
        attened_by=request.POST.get("Attended-by"),
        date=request.POST.get("date")
        )
        return True
    except Exception as e:
        print("update income error:",e)
        return False

def CustomSerializer(query):
    join=snookerIncome.objects.raw(query)
    data=[]
    for i in join:
        data.append({"id":i.id,"description":i.description,"attened_by":i.attened_by,"date":i.date,"total_income":i.total_income})
    print("data",data)
    return data