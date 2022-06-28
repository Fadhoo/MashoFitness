from pytest import Item
from .models import *
from django.core.files.storage import FileSystemStorage
from cafeteria.suppliers.models import Supplier


def UpdateInventory(request):
    print(request.POST.get("supplier-name"))
    try:
        print("photo is selected", request.FILES)
        if request.FILES:
            print("photo is selected", request.FILES['photos'])
            f = request.FILES["photos"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
        else:
            filename = "default.png"

        # print(request.POST.get("update-id"))
        # print(request.POST.get("net-price"))
        Inventory.objects.filter(id=request.POST.get("update-id")).update(
            inventory_unit_price=request.POST.get("unit-price"),
            inventory_net_price=request.POST.get("net-price"),
            inventory_purchased_quantity=request.POST.get("purchased-qty"),
            # inventory_sub_total=request.POST.get("sub-total"),
            inventory_item_total=request.POST.get(
                "item-total"),
            inventory_order_number=request.POST.get(
                "order-number"),
            inventory_reference_number=request.POST.get(
                "reference-number"),
            # inventory_stock_in_shop=request.POST.get("available-stock-inshop"),
            inventory_stock_available=request.POST.get(
                "available-stock"),
            supplier_id=Supplier.objects.filter(
                supplier_name=request.POST.get("supplier-name")).first(),
        )

        Purchases.objects.create(
            purchases_unit_price=request.POST.get("unit-price"),
            purchases_net_price=request.POST.get("net-price"),
            purchases_purchased_quantity=request.POST.get("purchased-qty"),
            # inventory_sub_total=request.POST.get("sub-total"),
            purchases_item_total=request.POST.get(
                "item-total"),
            purchases_order_number=request.POST.get(
                "order-number"),
            purchases_reference_number=request.POST.get(
                "reference-number"),
            # inventory_stock_in_shop=request.POST.get("available-stock-inshop"),
            purchases_stock_available=request.POST.get(
                "available-stock"),
            purchases_supplier_id=Supplier.objects.filter(
                supplier_name=request.POST.get("supplier-name")).first(),
            purchases_item_id=Items.objects.get(id=Inventory.objects.get(id=request.POST.get("update-id")).inventory_item_id.id)
        ).save()
        print("successfully updated inventory")
    except Exception as e:
        print("No data found {}".format(e))

# def purchases(request):
#     pass


def CustomerPurchasesSerializer(query):
    data = []
    for i in query:
        data.append(
            {
                "id": i.id,
                "inventory_order_number": i.inventory_id.inventory_order_number,
                "inventory_order_number": i.inventory_id.inventory_reference_number,
                "supplier_id": i.inventory_id.supplier_id.supplier_name,
                "inventory_item_total": i.inventory_id.inventory_item_total,
                "status": i.status,
                "create_date": i.create_date,
            }
        )
    return data


def AddReturnPurchases(request):
    try:
        PurchasesReturn.objects.create(
            available_stock=request.POST.get("unit-price"),
            return_stock=request.POST.get("net-price"),
            tatal_price=request.POST.get("purchased-qty"),
            # inventory_sub_total=request.POST.get("sub-total"),
            unit_price=request.POST.get(
                "item-total"),
            inventoryid=request.POST.get(
                "reference-number"),
            supplier_id=Supplier.objects.filter(
                supplier_name=request.POST.get("supplier-name")).first(),
        )

        # PurchasesReturn.objects.create(status='Returned', inventory_id=Inventory.objects.get(
            # id=request.POST.get("update-id"))).save()
        print("successfully Added Return Purchases")
    except Exception as e:
        print("No data found {}".format(e))
