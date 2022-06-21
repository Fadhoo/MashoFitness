
from cafeteria.Items.models import Items, NonStock
from cafeteria.purchases.models import Inventory
from cafeteria.salesTerminal.models import Order, OrderHistory



def CostomSerializer(stock=None,nonstock=None):
    if stock is None:
        stock=Items.objects.all()
        nonstock=NonStock.objects.all()
    data=list()
    for i in stock:
        
        data.append(
                {
            'id':i.id,
            'item_name':i.item_name,
            'item_price':i.item_selling_price,
            'item_category':i.item_category,
            'item_image':i.item_image.url,
        }
        )
    for i in nonstock:
        
        data.append(
            {
            'id':i.id,
            'item_name':i.nonStock_item_name,
            'item_price':i.nonStock_item_selling_price,
            'item_category':i.nonStock_item_category,
            'item_image':i.nonStock_item_image.url,
        }
        )
    return data


def OrderPlaced(dictonary:dict,order:Order):
    """
    {
        'itemName': 'juice',
        'quantity': '1',
        'discount': '', 
        'totalPrice': '200'
    }
    """
    if Items.objects.filter(item_name=dictonary["itemName"]).exists():
        inventory=Inventory.objects.get(inventory_item_id=Items.objects.get(item_name=dictonary["itemName"]))
        inventory.inventory_purchased_quantity-=int(dictonary["quantity"])
    elif NonStock.objects.filter(nonStock_item_name=dictonary["itemName"]).exists():
        pass
    discount=int(dictonary["discount"]) if dictonary["discount"] else 0
    price=int(dictonary["totalPrice"]) if dictonary["totalPrice"] else 0
    quantity=int(dictonary["quantity"]) if dictonary["quantity"] else 0
    price=(price+discount)//quantity
    total=(price*quantity)-discount
    print(price,quantity,discount,total)
    OrderHistory.objects.create(
        order_id=order,
        order_item_name=dictonary["itemName"],
        order_item_quantity=quantity,
        order_item_discount=discount,
        order_item_price=price,
        order_item_total=total,
    )

