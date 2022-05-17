from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("supplier/", views.supplier, name="supplier"),
    path("updateSupplier/", views.updateSupplier, name="updateSupplier"),
    

    # api path
]