from .models import Match, Booking, Team

def createDailyMatchTimeTable(date):
    
    if Booking.objects.filter(date=date).exists():
        return Booking.objects.filter(date=date)
        pass
    else:
        Booking.objects.create(date=date,time="12:00 to 1:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="1:00 to 2:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="2:00 to 3:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="3:00 to 4:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="4:00 to 5:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="5:00 to 6:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="6:00 to 7:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="7:00 to 8:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="8:00 to 9:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="9:00 to 10:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="10:00 to 11:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="11:00 to 12:00",meridiem="PM",status=False)
        Booking.objects.create(date=date,time="12:00 to 1:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="1:00 to 2:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="2:00 to 3:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="3:00 to 4:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="4:00 to 5:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="5:00 to 6:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="6:00 to 7:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="7:00 to 8:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="8:00 to 9:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="9:00 to 10:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="10:00 to 11:00",meridiem="AM",status=False)
        Booking.objects.create(date=date,time="11:00 to 12:00",meridiem="AM",status=False)

        return Booking.objects.filter(date=date)
