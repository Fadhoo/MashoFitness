from apscheduler.schedulers.background import BackgroundScheduler
from threading import Thread
from theme.models import Member
import requests
import datetime as dt
def send_sms(phoneNumber,message):
    phoneNumber=phoneNumber.replace("-", "")
    # print(phoneNumber)
    return requests.get(f'https://sendpk.com/api/sms.php?api_key=923402601866-e097c210-00f1-4fdf-9318-7e012f796e4a&sender=MashoFitness&mobile={phoneNumber}&message={message}').status_code
def main():
    try:
        if Member.objects.all().exists():
            for i in Member.objects.all():
                
                if (i.member_membership_expiry_date-dt.date.today()).days==5:
                    print('5 days left')
                    print(send_sms(i.member_contact, '5 days left'))
                elif (i.member_membership_expiry_date-dt.date.today()).days==3:
                    print('3 days left')
                    print(send_sms(i.member_contact, '3 days left'))
                elif (i.member_membership_expiry_date-dt.date.today()).days==1:
                    print('1 day left',)
                    print(send_sms(i.member_contact, '1 day left'))
                else:
                    print((i.member_membership_expiry_date-dt.date.today()).days)
    except Exception as e:
        print("checkMemberStarus exception",e)

def fun_call():
    Thread(target=main).start()
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fun_call, 'interval', minutes=3)
    scheduler.start()
