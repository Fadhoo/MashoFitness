from django.urls import path
from . import views

urlpatterns = [
    path('', views.Userlogin, name='login'),
    path('index/', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('createUser/', views.createUser, name='createUser'),
]