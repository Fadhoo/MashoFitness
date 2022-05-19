from .models import *
from django.core.files.storage import FileSystemStorage



def UpdateInventory(request):
    try:
        if request.FILES:
            f=request.FILES["photos"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"
        print(request.POST.get("update-id"))
        print(request.POST.get("net-price"))
        Inventory.objects.filter(id=request.POST.get("update-id")).update(
                                                    inventory_unit_price=request.POST.get("unit-price"),
                                                    inventory_net_price=request.POST.get("net-price"),
                                                    inventory_purchased_quantity=request.POST.get("purchased-qty"),
                                                    inventory_sub_total=request.POST.get("sub-total"),
                                                    inventory_item_total=request.POST.get("item-total"),
                                                    inventory_order_number=request.POST.get("order-number"),
                                                    inventory_reference_number=request.POST.get("reference-number"),
                                                    inventory_stock_in_shop=request.POST.get("available-stock"),)
        print("successfully updated inventory")
    except Exception as e:
        print("No data found {}".format(e))