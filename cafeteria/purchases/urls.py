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
]