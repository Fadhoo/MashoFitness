from .models import *
from django.core.files.storage import FileSystemStorage
from cafeteria.suppliers.models import Supplier



def UpdateInventory(request):
    print(request.POST.get("supplier-name"))
    try:
        print("photo is selected",request.FILES)
        if request.FILES:
            print("photo is selected",request.FILES['photos'])
            f=request.FILES["photos"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
        else:
            filename="default.png"
            
        # print(request.POST.get("update-id"))
        # print(request.POST.get("net-price"))  
        Inventory.objects.filter(id=request.POST.get("update-id")).update(
                                                    inventory_unit_price=request.POST.get("unit-price"),
                                                    inventory_net_price=request.POST.get("net-price"),
                                                    inventory_purchased_quantity=request.POST.get("purchased-qty"),
                                                    inventory_sub_total=request.POST.get("sub-total"),
                                                    inventory_item_total=request.POST.get("item-total"),
                                                    inventory_order_number=request.POST.get("order-number"),
                                                    inventory_reference_number=request.POST.get("reference-number"),
                                                    inventory_stock_in_shop=request.POST.get("available-stock"),
                                                    supplier_id=Supplier.objects.filter(supplier_name=request.POST.get("supplier-name")).first(),
                                                    )
        

        Purchases.objects.create(status='Completed', inventory_id=Inventory.objects.get(id=request.POST.get("update-id"))).save()
        print("successfully updated inventory")
    except Exception as e:
        print("No data found {}".format(e))

def purchases(request):
    pass