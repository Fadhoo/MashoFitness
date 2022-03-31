from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path('expensesReport/', views.expensesReport, name='expensesReport'),
    path('reports/', views.reports, name='reports'),
    path('rental/', views.rental, name="rental"),
    path('revenue/', views.revenue, name="revenue"),
    path('updateRental/', views.updateRental, name="updateRental"),


    # api paths
    path('api/deleteRentalRecord/', views.deleteRentalRecord, name='deleteRentalRecord'),
    path('api/SearchByRentalField/', views.SearchByRentalField, name='SearchByRentalField'),
    path('api/searchByRentalDate/', views.searchByRentalDate, name='searchByRentalDate'),
]

