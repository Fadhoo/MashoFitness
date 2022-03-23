from .models import *
from django.core.files.storage import FileSystemStorage

# create the item data  in database table name Items from models
def ItemsAdd(request):
    '''
    add_item=Items.objects.create(the column names defined in models one by one) # to create objects in a table
    add_item.save() # to save the item data into a table
    '''
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"

    

        add_item = Items.objects.create(item_code=request.POST.get("item-code"),
                        item_name=request.POST.get("item-name"), item_unit=request.POST.get("unit-measure"),
                        item_category=request.POST.get("item-category"), item_brand=request.POST.get("item-brand"),
                        item_manufacturer=request.POST.get("manufacturer"), item_selling_price=request.POST.get("selling-price"),
                        item_max_selling_quantity=request.POST.get("max-selling-qty"), item_min_selling_quantity=request.POST.get("min-selling-qty"),
                        item_reorder_level=request.POST.get("reorder-level"), item_image=filename,
                        item_description=request.POST.get("item-description"),
                        item_status=request.POST.get("status"), item_expiry_day=request.POST.get("remaining-days"),
                        )
        add_item.save()

        return add_item
    except Exception as e:
        print("Error in adding items", e)
        return False

# update the item data 
def UpdateItem(request):
    ''' a function that update the items from database
    if photo is selected by user
    fs = FileSystemStorage() to store the picture in system
    filename=fs.save(f.name,f) and save the file name 
    uploaded_file_url=fs.url(filename)
    else
    filename="default.png" the default png pic will save in database
    '''
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"
        print("update id recieved:",request.POST.get("update-id"))
        update_item = Items.objects.filter(id=request.POST.get("update-id")).update(item_code=request.POST.get("item-code"),
                        item_name=request.POST.get("item-name"), item_unit=request.POST.get("unit-measure"),
                        item_category=request.POST.get("item-category"), item_brand=request.POST.get("item-brand"),
                        item_manufacturer=request.POST.get("manufacturer"), item_selling_price=request.POST.get("selling-price"),
                        item_max_selling_quantity=request.POST.get("max-selling-qty"), item_min_selling_quantity=request.POST.get("min-selling-qty"),
                        item_reorder_level=request.POST.get("reorder-level"), item_image=filename,
                        item_description=request.POST.get("item-description"),
                        item_status=request.POST.get("status"), item_expiry_day=request.POST.get("remaining-days"),
                        )

        return update_item
    except Exception as e:
        print("Error in adding items", e)
        return False

# function for products to add in Product table 
def addProducts(request):
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"

        add_product =   Product.objects.create(product_code=request.POST.get("product-code"),
                        product_name=request.POST.get("product-name"), product_unit=request.POST.get("product-measure"),
                        product_category=request.POST.get("product-category"), product_brand=request.POST.get("product-brand"),
                        product_manufacturer=request.POST.get("manufacturer"), product_selling_price=request.POST.get("selling-price"),
                        product_max_selling_quantity=request.POST.get("max-selling-qty"), product_min_selling_quantity=request.POST.get("min-selling-qty"),
                        product_image=filename, product_expire_date=request.POST.get("expiry-date"), 
                        product_description=request.POST.get("item-description"), product_status=request.POST.get("status")
                        )
        add_product.save()

        return add_product
    except Exception as e:
        print("Error in adding items", e)
        return False

# function for non-stock items to add in NonStock table
def addNonStockItems(request):
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"

        add_nonStock_item = NonStock.objects.create(nonStock_item_code=request.POST.get("item-code"),
                        nonStock_item_name=request.POST.get("item-name"), 
                        nonStock_item_unit=request.POST.get("unit-measurement"),
                        nonStock_item_category=request.POST.get("item-category"), 
                        nonStock_item_brand=request.POST.get("item-brand"),
                        nonStock_item_manufacturer=request.POST.get("manufacturer"),
                        nonStock_item_purchase_price=request.POST.get("purchase-price"),
                        nonStock_item_selling_price=request.POST.get("selling-price"),
                        nonStock_item_max_selling_quantity=request.POST.get("max-selling-qty"), 
                        nonStock_item_min_selling_quantity=request.POST.get("min-selling-qty"),nonStock_item_image=filename, 
                        nonStock_item_description=request.POST.get("description"),
                        nonStock_item_status=request.POST.get("status")
                        )
        add_nonStock_item.save()

        return add_nonStock_item
    except Exception as e:
        print("Error in adding items", e)
        return False


# function for non-stock items to update the NonStock table's values
def updateNonStockItems(request):
    try:
        if request.FILES:
            f=request.FILES["photo"]
            fs = FileSystemStorage()
            filename = fs.save(f.name, f)
            uploaded_file_url = fs.url(filename)
        else:
            filename="default.png"
        print(request.POST.get("update-id"))
        update_nonStock_item = NonStock.objects.filter(id=request.POST.get("update-id")).update(nonStock_item_code=request.POST.get("item-code"),
                        nonStock_item_name=request.POST.get("item-name"), 
                        nonStock_item_unit=request.POST.get("unit-measurement"),
                        nonStock_item_category=request.POST.get("item-category"), 
                        nonStock_item_brand=request.POST.get("item-brand"),
                        nonStock_item_manufacturer=request.POST.get("manufacturer"),
                        nonStock_item_purchase_price=request.POST.get("purchase-price"),
                        nonStock_item_selling_price=request.POST.get("selling-price"),
                        nonStock_item_status=request.POST.get("status"),
                        nonStock_item_image=filename,  
                        nonStock_item_description=request.POST.get("description"),
                        nonStock_item_max_selling_quantity=request.POST.get("max-selling-qty"), 
                        nonStock_item_min_selling_quantity=request.POST.get("min-selling-qty"),
                        )

        return update_nonStock_item
    except Exception as e:
        print("Error in adding items", e)
        return False