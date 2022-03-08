
function reloadPage() {
    window.location.reload();
    console.log("reload");
};

function SearchByItemField() {
    let field = document.getElementById('search-by-field').value;
    let value = document.getElementById('search-by-value').value;
    if (field != '' && value != '') {
        $.ajax({
            method: "GET",
            url: "/api/SearchByItemField/",
            data: { "field": field, "value": value },
            success: function (data) {
                // console.log("success on search" + data);
                update_table(data)
            },
            error: function () {
                console.log('error');
            }

        })
    }
};


function update_table(data){
    console.log(data);
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        console.log(elem);
        row = '<tr class="text-left hover:bg-red-200">'+
                                    
        '<td class="p-2">'+

            '<div class="float-left hover:text-red-600">'+
                '<span  @click="openUpdateModal">'+
                    '<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">'+
                        '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />'+
                    '</svg>'+
                '</span>'+
            '</div>'+
        '</td>'+
        '<td class="p-2">'+elem['item_code']+'</td>'+
        '<td class="p-2">'+elem['item_name']+'</td>'+
        '<td class="p-2">'+elem['item_unit']+'</td>'+
        '<td class="p-2">'+elem['item_selling_price']+'</td>'+
        '<td class="p-2">'+elem['item_max_selling_quantity']+'</td>'+
        '<td class="p-2">'+elem['item_category']+'</td>'+
        '<td class="p-2">'+elem['item_status']+'</td>'+

        
    '</tr>'

    all_rows = all_rows + row;
    });
    $('#myTable tbody').html(all_rows);
}

function update_query_call(id){
    $.ajax({
        method: "GET",
        url: "/api/UpdateItemQueryCall/",
        data: { "id": id},
        success: function (data) {
            Object.keys(data).forEach(key => {
            elem = data[key];
            console.log(elem)
            
            document.getElementById("update-id").value=elem['id'];
            document.getElementById("item-code").value=elem['item_code'];
            document.getElementById("item-name").value=elem['item_name'];
            document.getElementById("item-unit").value=elem['item_unit'];
            document.getElementById("item-brand").value=elem['item_brand'];
            document.getElementById("item-category").value=elem['item_category'];
            document.getElementById("item-manufacturer").value=elem['item_manufacturer'];
            document.getElementById("item-selling-price").value=elem['item_selling_price'];
            document.getElementById("item-max-selling-qty").value=elem['item_max_selling_quantity'];
            document.getElementById("item-min-selling-qty").value=elem['item_min_selling_quantity'];
            document.getElementById("item-reorder-level").value=elem['item_reorder_level'];
            document.getElementById("image").src=elem['item_image'];
            // document.getElementById("item-barcode").value=elem['item_code'];
            document.getElementById("update-item-description").value=elem['item_description'];

            document.getElementById("update-status").value=elem['item_status'];
            document.getElementById("update-remaining-days").value=elem['item_expiry_day'];
            });
            
        },
        error: function () {
            console.log('error');
        }

    })
}

function update_query_call_nonstock(id){
    $.ajax({
        method: "GET",
        url: "/api/UpdateNonStockItemQueryCall/",
        data: { "nonStock-id": id},
        success: function (data) {
            Object.keys(data).forEach(key => {
            elem = data[key];
            console.log(elem)
            
            document.getElementById("update-id").value=elem['id'];

            document.getElementById("item-code").value=elem['nonStock_item_code'];
            document.getElementById("item-name").value=elem['nonStock_item_name'];
            document.getElementById("item-unit").value=elem['nonStock_item_unit'];
            document.getElementById("item-category").value=elem['nonStock_item_category'];
            document.getElementById("item-brand").value=elem['nonStock_item_brand'];
            document.getElementById("item-manufacturer").value=elem['nonStock_item_manufacturer'];
            document.getElementById("purchase-price").value=elem['nonStock_item_purchase_price'];
            document.getElementById("item-selling-price").value=elem['nonStock_item_selling_price'];
            document.getElementById("update-status").value=elem['nonStock_item_status'];
            document.getElementById("image").src=elem['nonStock_item_image'];
            document.getElementById("item-description").value=elem['nonStock_item_description'];
            document.getElementById("max-selling-qty").value=elem['nonStock_item_max_selling_quantity'];
            document.getElementById("min-selling-qty").value=elem['nonStock_item_min_selling_quantity'];
            // document.getElementById("item-barcode").value=elem['item_code'];

            });
            
        },
        error: function () {
            console.log('error');
        }

    })
}
