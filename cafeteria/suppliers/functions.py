from .models import Supplier

def addSupplier(request):
    try:
        add_supplier = Supplier.objects.create(supplier_account=request.POST.get("supplier-account"),
                        supplier_name=request.POST.get("supplier-name"),
                        supplier_contact=request.POST.get("supplier-contact"),
                        supplier_email=request.POST.get("supplier-email"),
                        supplier_status=request.POST.get("supplier-status"),
                        supplier_address=request.POST.get("supplier-address"),
                        supplier_city=request.POST.get("supplier-city"),
                        supplier_country=request.POST.get("supplier-country")
                        )
        add_supplier.save()

        return add_supplier
    except Exception as e:
        print("Error in adding supplier data", e)
        return False

def updateSupplierData(request):
    try:
        Supplier.objects.filter(id=request.POST.get("update-id")).update(
                        supplier_account=request.POST.get("supplier-account"),
                        supplier_name=request.POST.get("supplier-name"),
                        supplier_contact=request.POST.get("supplier-contact"),
                        supplier_email=request.POST.get("supplier-email"),
                        supplier_status=request.POST.get("supplier-status"),
                        supplier_address=request.POST.get("supplier-address"),
                        supplier_city=request.POST.get("supplier-city"),
                        supplier_country=request.POST.get("supplier-country")
                        )
    except Exception as e:
        print("Error in updating supplier data", e)
        return False
