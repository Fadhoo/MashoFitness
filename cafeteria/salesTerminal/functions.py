from cafeteria.Items.models import Items, NonStock



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
