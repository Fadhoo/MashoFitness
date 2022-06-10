member_id=null;
item_name = [];
function addToCart(id) {
    $.ajax({
        url: '/api/salesTerminal/addToCart',
        type: 'GET',
        data: {
            id: id
        },
        success: function (data) {
            CreateRows(data,id);
            updateCart();
        }
    });

}


function CreateRows(data,id) {
    try{
    if (item_name.includes(data['inventory_item_id']['item_name'])) {
        alert("Item already in cart");
    }
    else {
        item_name.push(data['inventory_item_id']['item_name']);
        $('#myTable').find('tbody').append(
            '<tr class="border-2 text-center">' +
            '<td id="DeleteRow">' +
            '<svg xmlns="http://www.w3.org/2000/svg"' +
            'class="h-5 w-5 hover:border-blue-800 border-2 rounded-md text-red-900 cursor-pointer"' +
            'fill="none" viewBox="0 0 24 24"' +
            'stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round"' +
            'stroke-width="2" d="M6 18L18 6M6 6l12 12" />' +
            '</svg>' +
            '</td>' +
            '<td class="p-1">1</td>' +
            '<td class="p-1">' + data['inventory_item_id']['item_code'] + '</td>' +
            '<td class="p-1 product-name">' + data['inventory_item_id']['item_name'] + '</td>' +
            '<td class="p-1 productPrice">' + data['inventory_item_id']['item_selling_price'] + '</td>' +
            '<td class="p-1 quantity">1</td>' +
            '<td class="p-1 inline-flex items-center space-x-1">' +
            '<svg xmlns="http://www.w3.org/2000/svg" class="sub-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6" />' +
            '</svg>' +

            ' <svg xmlns="http://www.w3.org/2000/svg" class="add-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />' +
            '</svg>' +
            '</td>' +
            '<td class="totaldiscount p-1"><input placeholder="0" class="discount w-10"  /></td>' +
            '<td class="price p-1 font-semibold">' + data['inventory_item_id']['item_selling_price'] + '</td>' +
            '</tr>'
        );
    }}
    catch(err){
        $.ajax({
            url: '/api/salesTerminal/addToCartNonStock',
            type: 'GET',
            data: {
                id: id
            },
            success: function (data) {
                CreateNonStockRows(data);
                updateCart();
            }
        });
    }
}

function CreateNonStockRows(data) {
    if (item_name.includes(data['nonStock_item_name'])) {
        alert("Item already in cart");
    }
    else {
        item_name.push(data['nonStock_item_name']);
        $('#myTable').find('tbody').append(
            '<tr class="border-2 text-center">' +
            '<td id="DeleteRow">' +
            '<svg xmlns="http://www.w3.org/2000/svg"' +
            'class="h-5 w-5 hover:border-blue-800 border-2 rounded-md text-red-900 cursor-pointer"' +
            'fill="none" viewBox="0 0 24 24"' +
            'stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round"' +
            'stroke-width="2" d="M6 18L18 6M6 6l12 12" />' +
            '</svg>' +
            '</td>' +
            '<td class="p-1">1</td>' +
            '<td class="p-1">' + data['nonStock_item_code'] + '</td>' +
            '<td class="p-1 product-name">' + data['nonStock_item_name'] + '</td>' +
            '<td class="p-1 productPrice">' + data['nonStock_item_selling_price'] + '</td>' +
            '<td class="p-1 quantity">1</td>' +
            '<td class="p-1 inline-flex items-center space-x-1">' +
            '<svg xmlns="http://www.w3.org/2000/svg" class="sub-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 12H6" />' +
            '</svg>' +

            ' <svg xmlns="http://www.w3.org/2000/svg" class="add-btn h-5 w-5 border border-blue-400 hover:border-2 rounded-md cursor-pointer" fill="none" viewBox="0 0 24 24" stroke="currentColor">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />' +
            '</svg>' +
            '</td>' +
            '<td class="totaldiscount p-1"><input placeholder="0" class="discount w-10"  /></td>' +
            '<td class="price p-1 font-semibold">' + data['nonStock_item_selling_price'] + '</td>' +
            '</tr>'
        );
    }



}



$(document).ready(function () {
    // code to read selected table row cell data (values).
    $("#myTable").on('click', '.sub-btn', function () {
        // get the current row
        var currentRow = $(this).closest("tr");
        var col4 = currentRow.find("td:eq(4)").text(); // get current row 4thTD
        var count = parseInt(currentRow.find("td:eq(5)").text()) - 1; // get current row 5thTD
        currentRow.find("td:eq(5)").text(count);
        currentRow.find("td:eq(8)").text(count * col4); // get current row 4thTD
        updateCart();
        //  console.log(col4);
    });
    $("#myTable").on('click', '.add-btn', function () {
        // get the current row
        var currentRow = $(this).closest("tr");
        var col4 = currentRow.find("td:eq(4)").text(); // get current row 4thTD
        var count = parseInt(currentRow.find("td:eq(5)").text()) + 1; // get current row 5thTD
        currentRow.find("td:eq(5)").text(count);
        currentRow.find("td:eq(8)").text(count * col4); // get current row 4thTD
        updateCart();
    });

});


(function () {
    "use strict";

    $("table").on("change", "input", function () {
        var row = $(this).closest("tr");
        var discount = parseFloat(row.find(".discount").val());
        var price = parseFloat(row.find(".price").text());
        var quantity = parseFloat(row.find(".quantity").text());
        var productprice=parseFloat(row.find(".productPrice").text());
        if (isNaN(discount)) {
            discount = 0;
            row.find(".price").text(productprice*quantity);
            updateCart();
        }
        else{
        var total = price - discount;
        row.find(".price").text(total);
        updateCart();}
    });
})();

$("#myTable").on("click", "#DeleteRow", function () {
    item_name.pop($(this).closest("tr").find(".product-name").text());
    $(this).closest("tr").remove();
    updateCart();

});

function updateCart() {
    const rows = document.querySelectorAll("#myTableBody > tr");
    var total = 0;
    var discount = 0;
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        if (row.querySelectorAll("td > input")[0].value != "") {
            discount += parseFloat(row.querySelectorAll("td > input")[0].value);
        }
        total += parseFloat(row.querySelector(".price").textContent);
    }
    document.getElementById("total-price").innerHTML = total ; //total;
    document.getElementById("total-discount").innerHTML = discount; //total discount
    document.getElementById("subtotal").innerHTML = total + discount; //subtotal
    document.getElementById("amount-paid").innerHTML = total ;
}


function searchItemInSalesTerminal(value) {
    $.ajax({
        url: '/api/searchItemInSalesTerminal/',
        method: 'GET',
        data: {
            'item_name': value
        },
        success: function (data) {
            $('#item-main-div').empty();
            if (data['Stock']) {
                Object.keys(data['Stock']).forEach(key => {
                    $('#item-main-div').append(
                        '<div onclick="addToCart(' + data['Stock'][key]["id"] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['Stock'][key]['item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' + data['Stock'][key]['item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['Stock'][key]['item_selling_price'] + '</span>' +
                        '<img src=' + data['Stock'][key]['item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
                })

            }
            else if (data['NonStock']) {
                Object.keys(data['NonStock']).forEach(key => {
                $('#item-main-div').append(
                    '<div onclick="addToCart(' + data['NonStock'][key]["id"] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['NonStock'][key]['nonStock_item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' + data['NonStock'][key]['nonStock_item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['NonStock'][key]['nonStock_item_selling_price'] + '</span>' +
                        '<img src=' + data['NonStock'][key]['nonStock_item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
                })
            }
            else {
                // console.log(data);
                Object.keys(data['Both']).forEach(key => {
                $('#item-main-div').append(
                    '<div onclick="addToCart(' + data['Both'][key]['id'] + ')"' +
                        'class="px-3 py-3 flex flex-col hover:border-2 border-blue-200 cursor-pointer bg-gray-200 rounded-md h-32 justify-between">' +
                        '<div>' +
                        '<div class="font-bold text-gray-800">' + data['Both'][key]['item_name'] + '</div>' +
                        '<span class="font-light text-sm text-gray-400">' +data['Both'][key]['item_category'] + '</span>' +
                        '</div>' +
                        '<div class="flex flex-row justify-between items-center">' +
                        '<span class="self-end font-bold text-lg text-yellow-500">' + data['Both'][key]['item_price'] + '</span>' +
                        '<img src=' + data['Both'][key]['item_image'] + ' class="h-14 object-cover rounded-md" alt="">' +
                        '</div></div>');
            })
            }
        }
    });
}

function onlyOne(checkbox) {
    var checkboxes = document.getElementsByName('check')
    checkboxes.forEach((item) => {
        if (item !== checkbox) item.checked = false
    })
    member_id = checkbox.value
    // console.log(member_id)
}

function memberSelection(){
    console.log(member_id)
    const rows = document.querySelectorAll("#memberTableId > tr");
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        id=row.querySelectorAll("td > input")[0].value
        // console.log(row.querySelector(".member-name-row").textContent)
        if (id==member_id) {
            console.log(row.querySelector(".member-name-row").textContent)
            document.getElementById("Member-name").innerHTML =row.querySelector(".member-name-row").textContent;
        }
    }

}

function MemberSearchByName(){
    $.ajax({
        url: '/api/searchbyname/',
        method: 'GET',
        data: {
            'searchbyname': document.getElementById("search-memberName").value
        },
        success: function (data) {
            console.log(data);
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        row =
        '<tr class="border-2 hover:bg-slate-300">' +
            '<td class="p-2">' +
                '<input onclick="requestDelete(this)" data-id="' + elem['id'] +'" type="checkbox" class="cursor-pointer rounded-md" onc>' +
            '</td>' +
            '<td class="p-2">'+ elem['member_serial_no'] +'</td>'+
            '<td class="p-2"><div class="flex items-center text-sm">'+
                    '<div class="relative hidden w-8 h-8 mr-3 rounded-full md:block">'+
                        '<img class="object-cover w-full h-full rounded-full"'+ 
                           ' src="'+ elem['member_image'] +'"'+
                            'alt="" loading="lazy" />'+
                        '<div class="absolute inset-0 rounded-full shadow-inner"'+
                            'aria-hidden="true"></div>'+
                    '</div>'+
                    '<div>'+
                        '<p class="font-semibold">'+ elem['member_name'] +'</p>'+
                        '<p class="text-sm text-gray-600 ">'+elem['member_membership_id']['category_name']+'</p>'+
                    '</div>'+
                '</div>'+
            '</td>'+
            '<td class="p-2">'+elem['member_card_id']+'</td>'+
            '<td class="p-2">'+elem['member_contact']+'</td>'+
            '<td class="p-2">'+elem['member_membership_id']['category_months']+'</td>'+
            '<td class="p-2">'+'Masho'+'</td>'+
            '<td class="p-2">'+ elem['member_membership_start_date'] +'</td>'+
            '<td class="p-2">'+elem['member_membership_expiry_date']+'</td>'+
            '<td class="p-2">'+
                '<span class="px-2 py-1 font-semibold leading-tight text-black bg-blue-400 rounded-full">'+ elem['active_fee_id']['status']+ '</span>'+
            '</td>'+
            
            '<td class="p-2" >'+
                '<div class="float-right mr-5">'+
                    '<a href="/memberDetails/?data='+elem['id']+'">'+
                        '<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 cursor-pointer"'+
                            'fill="none" viewBox="0 0 24 24" stroke="currentColor" >'+
                            '<path stroke-linecap="round" stroke-linejoin="round"'+
                                'stroke-width="2"'+
                                'd="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />'+
                        '</svg>'+
                    '</a>'+
                '</div>'+
            '</td>'+
            
            '<td class="p-2">'+
            '<button @click="openSMSModal('+elem['id']+');"'+
                    'class="bg-green-500 drop-shadow-md px-5 rounded-lg rounded-br-none">SMS</button>'+
            '</td>'+
        '</tr>';
       
        all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
        },
        error: function (data) {
            console.log(data)
        }
    });
}