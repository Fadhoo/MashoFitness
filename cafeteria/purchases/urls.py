from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("inventory/", views.inventory, name="inventory"),
    path("purchaseReturn/", views.purchaseReturn, name="purchasesReturn"),
    path("purchases/", views.purchases, name="purchases"),
    # # api path
    path("api/updateInventoryQueryCall/", views.updateInventoryQueryCall, name='updateInventoryQueryCall'),
    path('api/salesTerminal/addToCart/', views.addToCart, name='addToCart'),
    path('api/salesTerminal/addToCartNonStock/', views.addToCartNonStock, name='addToCartNonStock'),
    path('api/cafeteria/inventory/search_inventory_ItemName/',views.search_inventory_ItemName,name='search item name in inventory'),
    path("api/cafeteria/inventory/search_inventory_ItemCode/",views.search_inventory_ItemCode,name="item code search"),
    path("api/cafeteria/purchases/search_purchases_supplierName/",views.search_purchases_supplierName,name="purchases supplier search"),
    path("api/cafeteria/purchases/search_purchases_orderNumber/",views.search_purchases_orderNumber,name="purchases order search"),




]