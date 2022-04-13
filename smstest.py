import requests

r =requests.get('https://sendpk.com/api/sms.php?api_key=923402601866-e097c210-00f1-4fdf-9318-7e012f796e4a&sender=MashoFitness&mobile=03352321360&message=Masho Fitness is a fitness club in Karachi. You can book your slot here')
print(r.text)
print(r.status_code)