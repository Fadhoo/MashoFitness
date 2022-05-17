from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("salesTerminal/", views.salesTerminal, name="salesTerminal"),

    # api path
]