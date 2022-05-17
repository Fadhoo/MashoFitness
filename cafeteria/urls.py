from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("addItem/", views.addItem, name="addItem"),
    path("addNonStockItem/", views.addNonStockItem, name="addNonStockItem"),
    path("customer/", views.customer, name="customer"),
    path("updateCustomer/", views.updateCustomer, name="updateCustomer"),
    path("inventory/", views.inventory, name="inventory"),
    path("pos/", views.pos, name="pos"),
    path("purchasesReturn/", views.purchasesReturn, name="purchasesReturn"),
    path("purchases/", views.purchases, name="purchases"),
    path("sales/", views.sales, name="sales"),
    path("salesReturn/", views.salesReturn, name="salesReturn"),
    path("salesTerminal/", views.salesTerminal, name="salesTerminal"),
    path("supplier/", views.supplier, name="supplier"),
    path("updateSupplier/", views.updateSupplier, name="updateSupplier"),
    path("cafeteriaExpenses/", views.cafeteriaExpenses, name="cafeteriaExpenses"),
    path("updateCafeteriaExpenses/", views.updateCafeteriaExpenses, name="updateCafeteriaExpenses"),
    path("barcodeLabel/", views.barcodeLabel, name="barcodeLabel"),
    

    # api path
    path("api/SearchByItemField/", views.SearchByItemField, name='SearchByItemField'),
    path("api/SearchByStockField/", views.SearchByStockField, name='SearchByStockField'),
    path("api/UpdateItemQueryCall/", views.UpdateItemQueryCall, name='UpdateItemQueryCall'),
    path("api/UpdateNonStockItemQueryCall/", views.UpdateNonStockItemQueryCall, name='UpdateNonStockItemQueryCall'),
    path("api/InventoryQueryCall/", views.InventoryQueryCall, name='InventoryQueryCall'),
]