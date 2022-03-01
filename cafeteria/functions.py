from .models import *



def ItemsAdd(request):
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"

        add_item = addItems.objects.create(item_code=request.POST.get("item-code"),
                        item_name=request.POST.get("item-name"), item_unit=request.POST.get("unit-measure"),
                        item_category=request.POST.get("item-category"), item_brand=request.POST.get("item-brand"),
                        item_manufacturer=request.POST.get("manufacturer"), item_selling_price=request.POST.get("selling-price"),
                        item_max_selling_quantity=request.POST.get("max-selling-qty"), item_min_selling_quantity=request.POST.get("min-selling-qty"),
                        item_reorder_level=request.POST.get("reorder-level"), item_iamge=filename,
                        search_tag=request.POST.get("search-tag"), item_description=request.POST.get("item-description"),
                        item_status=request.POST.get("status"), item_expiry=request.POST.get("item-expiry"),
                        )

        return add_item
    except Exception as e:
        print("Error in adding items", e)
        return False