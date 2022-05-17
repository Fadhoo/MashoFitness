from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("inventory/", views.inventory, name="inventory"),
    path("purchaseReturn/", views.purchaseReturn, name="purchasesReturn"),
    path("purchases/", views.purchases, name="purchases"),
    # # api path
    path("api/InventoryQueryCall/", views.InventoryQueryCall, name='InventoryQueryCall'),
]