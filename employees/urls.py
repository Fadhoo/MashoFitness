from django.urls import path
from . import views
from theme.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('createUser/', views.createUser, name='createUser'),
]