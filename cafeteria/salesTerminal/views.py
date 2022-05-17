from django.shortcuts import render

# Create your views here.

def salesTerminal(request):
    return render(request, "salesTerminal.html")