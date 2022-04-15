from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import SmsModle
from .serializer import SmsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def smshistory(request):
    if request.method=="POST":
        if request.POST.get('add-sms'):
            SmsModle.objects.create(smsFor=request.POST.get('sms-for'),smsModule=request.POST.get('sms-module'),smsText=request.POST.get('sms-text')).save()
            return HttpResponseRedirect(reverse('smshistory'))
        if request.POST.get('sms-delete'):
            SmsModle.objects.filter(id=request.POST.get('sms-id')).delete()
            return HttpResponseRedirect(reverse('smshistory'))
    else:
        return render(request, 'smshistory.html',
        {'sms_list':SmsModle.objects.all()})
        

@api_view(['GET'])
def smsForsearch(request):
    if request.method == 'GET':
        try:
            module=request.GET.get('module')
            sms_list = SmsModle.objects.filter(smsModule=module)
            serializer = SmsSerializer(sms_list, many=True)
            return Response(serializer.data)
        except SmsModle.DoesNotExist:
            return Response("No sms module data found")
    else:
        return Response("Invalid request method")