from .models import Match, Booking, Team

def createDailyMatchTimeTable(date):
    
    if Booking.objects.filter(booking_date=date).exists():
        print("booking date already exist:")
        return Booking.objects.filter(booking_date=date)
    else:
        print("booking date not exist: craate new booking")
        Booking.objects.create(booking_date=date,time="12:00 to 1:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="1:00 to 2:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="2:00 to 3:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="3:00 to 4:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="4:00 to 5:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="5:00 to 6:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="6:00 to 7:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="7:00 to 8:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="8:00 to 9:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="9:00 to 10:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="10:00 to 11:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="11:00 to 12:00",meridiem="PM",status=False)
        Booking.objects.create(booking_date=date,time="12:00 to 1:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="1:00 to 2:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="2:00 to 3:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="3:00 to 4:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="4:00 to 5:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="5:00 to 6:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="6:00 to 7:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="7:00 to 8:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="8:00 to 9:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="9:00 to 10:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="10:00 to 11:00",meridiem="AM",status=False)
        Booking.objects.create(booking_date=date,time="11:00 to 12:00",meridiem="AM",status=False)

        return Booking.objects.filter(booking_date=date)

def addBook(request):
    team1=Team.objects.filter(team_name=request.POST.get("team-name"))[0]
    team2=Team.objects.filter(team_name=request.POST.get("team-name"))[0]
    booking_time=Booking.objects.filter(booking_date=request.POST.get("booking-date"))[0]
    match = Match.objects.create(date=request.POST.get("date"), fee=request.POST.get("fee"), 
            paid=request.POST.get("status"), team1=team1, team2=team2, booking_time=booking_time)

    return match

