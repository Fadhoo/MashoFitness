from django.urls import path
from . import views
from theme.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path('expensesReport/', views.expensesReport, name='expensesReport'),
    path('reports/', views.reports, name='reports'),
    path('rental/', views.rental, name="rental"),
    path('revenue/', views.revenue, name="revenue"),
    path('updateRental/', views.updateRental, name="updateRental"),
]

