from django.urls import path, include
from django.contrib import admin
from . import views
from theme.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("addItem/", views.addItem, name="addItem"),
    path("addNonStockItem/", views.addNonStockItem, name="addNonStockItem"),
    path("addProducts/", views.addProducts, name="addProducts"),
    path("customer/", views.customer, name="customer"),
    path("inventory/", views.inventory, name="inventory"),
    path("pos/", views.pos, name="pos"),
    path("purchasesReturn/", views.purchasesReturn, name="purchasesReturn"),
    path("purchases/", views.purchases, name="purchases"),
    path("sales/", views.sales, name="sales"),
    path("salesReturn/", views.salesReturn, name="salesReturn"),
    path("salesTerminal/", views.salesTerminal, name="salesTerminal"),
    path("supplier/", views.supplier, name="supplier"),
    
]