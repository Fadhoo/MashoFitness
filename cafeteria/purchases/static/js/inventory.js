add_array = null;
// function requestAdd(e) {
//     if (e.checked) {
//         add_array.push(parseInt(e.dataset.id));
//     } else {
//         add_array.splice(add_array.indexOf(e.dataset.id), 1);
//     }
    
// }

function update_query_call_inventory(id){
    $.ajax({
        method: "GET",
        url: "/api/updateInventoryQueryCall/",
        data: { "inventory-id": id },
        success: function (data) {
            Object.keys(data).forEach(key => {
            elem = data[key];
            console.log(elem['inventory_unit_price']['item_image'])
            
            document.getElementById("update-id").value=elem['id'];
            document.getElementById("item-code").value=elem['inventory_item_id']['item_code'];
            document.getElementById("item-name").value=elem['inventory_item_id.item_name'];
            document.getElementById("item-unit").value=elem['inventory_item_id.item_unit'];
            document.getElementById("unit-price").value=elem['inventory_unit_price'];
            document.getElementById("image").src=elem['inventory_unit_price']['item_image'];
            document.getElementById("net-price").value=elem['inventory_net_price'];
            document.getElementById("purchased-qty").value=elem['inventory_purchased_quantity'];
            document.getElementById("sub-total").value=elem['inventory_sub_total'];
            document.getElementById("item-total").value=elem['inventory_item_total'];
            document.getElementById("order-number").value=elem['inventory_order_number'];
            document.getElementById("reference-number").value=elem['inventory_reference_number'];
            document.getElementById("supplier").value=elem['supplier_id']['supplier_name'];
            document.getElementById("available-stock").value=elem['inventory_stock_in_shop'];
            });
            
        },
        error: function () {
            console.log('error');
        }

    })
}
function addInventoryItem(){
    // console.log(add_array)
    $.ajax({
        method: "GET",
        url: "/api/updateInventoryQueryCall/",
        data: { "inventory-id": add_array },
        success: function (data) {
            // console.log(data)
            Object.keys(data).forEach(key => {
            elem = data[key];
            console.log(elem['inventory_item_id']['item_image'])
            
            document.getElementById("update-id").value=elem['id'];
            document.getElementById("item-code").value=elem['inventory_item_id']['item_code'];
            document.getElementById("item-name").value=elem['inventory_item_id']['item_name'];
            document.getElementById("item-unit").value=elem['inventory_item_id']['item_unit'];
            document.getElementById("unit-price").value=elem['inventory_unit_price'];
            document.getElementById("image").src=elem['inventory_item_id']['item_image'];
            document.getElementById("net-price").value=elem['inventory_net_price'];
            document.getElementById("purchased-qty").value=elem['inventory_purchased_quantity'];
            document.getElementById("sub-total").value=elem['inventory_sub_total'];
            document.getElementById("item-total").value=elem['inventory_item_total'];
            document.getElementById("order-number").value=elem['inventory_order_number'];
            document.getElementById("reference-number").value=elem['inventory_reference_number'];
            document.getElementById("supplier").value=elem['supplier_id']['supplier_name'];
            document.getElementById("available-stock").value=elem['inventory_stock_in_shop'];
            });
            
        },
        error: function () {
            console.log('error');
        }

    })
}

function onlyOne(checkbox) {
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
add_array=parseInt(checkbox.dataset.id);
}

function ImageLoder(data){
    let file = data.files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
            console.log("update call ",e.target.result);
            document.getElementById('image').src = e.target.result;
            document.getElementById('update-image').src = e.target.result;
        }
    reader.readAsDataURL(file);

}
//  calculating the total price values 
document.getElementById("purchased-qty").onchange = function () {
    var unit_price = document.getElementById('unit-price').value;
    var purchased = document.getElementById('purchased-qty').value;
    var total = unit_price * purchased;
    document.getElementById('item-total').value = total;
};
