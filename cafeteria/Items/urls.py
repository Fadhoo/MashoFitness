from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("addItem/", views.addItem, name="addItem"),
    path("addNonStockItem/", views.addNonStockItem, name="addNonStockItem"),
    path("pos/", views.pos, name="pos"),
    path("cafeteriaExpenses/", views.cafeteriaExpenses, name="cafeteriaExpenses"),
    path("updateCafeteriaExpenses/", views.updateCafeteriaExpenses, name="updateCafeteriaExpenses"),
    path("barcodeLabel/", views.barcodeLabel, name="barcodeLabel"),
    

    # api path
    path("api/SearchByItemField/", views.SearchByItemField, name='SearchByItemField'),
    path("api/SearchByStockField/", views.SearchByStockField, name='SearchByStockField'),
    path("api/UpdateItemQueryCall/", views.UpdateItemQueryCall, name='UpdateItemQueryCall'),
]