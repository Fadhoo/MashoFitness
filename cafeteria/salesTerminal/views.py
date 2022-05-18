from django.shortcuts import render
from cafeteria.Items.models import Items, NonStock
# Create your views here.

def salesTerminal(request):
    data = Items.objects.all().first()
    print(data.item_name)
    return render(request, "salesTerminal.html", {
                            "itemsData": Items.objects.all(),
                            "nonStockItems": NonStock.objects.all()
                            })