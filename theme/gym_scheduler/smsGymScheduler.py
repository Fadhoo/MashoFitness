from apscheduler.schedulers.background import BackgroundScheduler
from threading import Thread
from theme.models import Member
import requests
import datetime as dt

def sendMessageToUser(name,number,message):
    number=number.replace("-", "")
    try:
        return requests.get(f'https://sendpk.com/api/sms.php?api_key=923402601866-e097c210-00f1-4fdf-9318-7e012f796e4a&sender=MashoFitness&mobile={number}&message=Dear {name},{message}').status_code
    except Exception as e:
        print("sendMessageToUser exception",e)

# def send_sms(phoneNumber,message):
#     phoneNumber=phoneNumber.replace("-", "")
#     print(phoneNumber)
    # return requests.get(f'https://sendpk.com/api/sms.php?api_key=923402601866-e097c210-00f1-4fdf-9318-7e012f796e4a&sender=MashoFitness&mobile={phoneNumber}&message={message}').status_code
def main():
    try:
        if Member.objects.all().exists():
            for i in Member.objects.all():
                
                if (i.member_membership_expiry_date-dt.date.today()).days==5:
                    print('5 days left')
                    # print(sendMessageToUser(i.member_name,i.member_contact, '5 days left'))
                elif (i.member_membership_expiry_date-dt.date.today()).days==3:
                    print('3 days left')
                    # print(sendMessageToUser(i.member_name,i.member_contact, '3 days left'))
                elif (i.member_membership_expiry_date-dt.date.today()).days==1:
                    print('1 day left',)
                    # print(sendMessageToUser(i.member_name,i.member_contact, '1 day left'))
                elif (i.member_membership_expiry_date-dt.date.today()).days==1:
                    print('0 day left',)
                    # print(sendMessageToUser(i.member_name,i.member_contact, 'today expire')
    except Exception as e:
        print("checkMemberStarus exception",e)

def fun_call():
    Thread(target=main).start()
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fun_call, 'interval', minutes=1440)
    scheduler.start()
