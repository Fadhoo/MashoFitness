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


def addCustomer(request):
    try:
        add_customer = Customer.objects.create(customer_account=request.POST.get("customer-account"),
                        customer_name=request.POST.get("customer-name"),
                        customer_contact=request.POST.get("customer-contact"),
                        customer_email=request.POST.get("customer-email"),
                        customer_status=request.POST.get("customer-status"),
                        customer_address=request.POST.get("customer-address"),
                        customer_city=request.POST.get("customer-city"),
                        customer_country=request.POST.get("customer-country")
                        )
        add_customer.save()

        return add_customer
    except Exception as e:
        print("Error in adding customer data", e)
        return False


def updateCustomerData(request):
    try:
        Customer.objects.filter(id=request.POST.get("update-id")).update(
                        customer_account=request.POST.get("customer-account"),
                        customer_name=request.POST.get("customer-name"),
                        customer_contact=request.POST.get("customer-contact"),
                        customer_email=request.POST.get("customer-email"),
                        customer_status=request.POST.get("customer-status"),
                        customer_address=request.POST.get("customer-address"),
                        customer_city=request.POST.get("customer-city"),
                        customer_country=request.POST.get("customer-country")
                        )
    except Exception as e:
        print("Error in updating customer data", e)
        return False