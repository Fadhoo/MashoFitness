from django.urls import path
from . import views
from theme.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path('income/', views.income, name='income'),
    path('reports/', views.reports, name='reports'),
    path('rental/', views.rental, name="rental")
]
