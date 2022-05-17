from django.urls import URLPattern, path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("sales/", views.sales, name="sales"),
    path("salesReturn/", views.salesReturn, name="salesReturn"),
]