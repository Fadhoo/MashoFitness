var delete_array = [];

function instalmentValueChanged(instalment) {
    var paidamount = document.getElementById("paidamount");
    // var remainingamount = document.getElementById("remainingamount");
    paidamount.style.display = instalment.checked ? "block" : "none";
    // remainingamount.style.display = instalment.checked ? "block" : "none";

};

function categoryClassChange(){
    let category_name=document.getElementById("membershipcategory").value
    let category_class=document.getElementById("membership-class").value
    let category_gender=document.getElementById("gender").value


    $.ajax({
        method: "GET",
        url: "/api/get_membershipCategory/",
        data:{
            "category_name":category_name,
            "category_class":category_class,
            "category_gender":category_gender
        },
        success: function (data) {
            Object.keys(data).forEach(key => {
                var value = data[key];
                document.getElementById("category-months").value=value['category_months'];
                document.getElementById("amount").value=value["category_fee"];
                document.getElementById("payableamount").value=value["category_fee"];
                getExpiry(value['category_months']);

            });
        },
        error: function () {
            console.log("error on get Membership Category months");
        }
    });



}


// document.getElementById('membership').onchange = function () {


//     $.ajax({
//         method: "GET",
//         url: "/api/get_membershipCategory/",
//         data: {
//             category_name: document.getElementById('membershipcategory').value,
//             months: String(this.value)
//         },

//         success: function (data) {
//             console.log("success on get Membership Category months" + data);
//             Object.keys(data).forEach(key => {
//                 var value = data[key];
//                 document.getElementById('amount').value = value["monthly_fee"];
//             });
//             getExpiry(this.value);


//         },
//         error: function () {
//             console.log("error on get Membership Category months");
//         }
//     });
// };


document.getElementById("discount").onchange = function () {
    var amount = document.getElementById('amount').value;
    var discount = document.getElementById('discount').value;
    var total = amount - discount;
    document.getElementById('payableamount').value = total;
};

document.getElementById("dateofbirth").onchange = function () {
    var Bdate = this.value;
    var Bday = +new Date(Bdate);
    document.getElementById('age').value = ~~((Date.now() - Bday) / (31557600000));
}

function getExpiry(data) {
    var expiry = new Date();
    var getmonth = data 
    
    getmonth = parseInt(getmonth.replace(/[^\d.]/g, ''));
    expiry.setMonth(expiry.getMonth() + getmonth);
    document.getElementById('expiry').value = expiry.toISOString().slice(0, 10);
}

document.getElementById("paidamounts").onchange = function(){
    let payableamount = document.getElementById("payableamount").value;
    let paidamount = document.getElementById("paidamounts").value;
    let remainingamount = payableamount - paidamount
    document.getElementById("remaining-amount").value = remainingamount;
    
};

// function payableOnChange(this){
//     let paidamount = document.getElementById("paid-amount").value;
//     alert(this.value)
//     alert(paidamount)
//     document.getElementById("remaining-amount").value=this.value - paidamount;
// }



function requestDelete(e) {
    console.log(delete_array);
    if (e.checked) {
        delete_array.push(parseInt(e.dataset.id));
    } else {
        delete_array.splice(delete_array.indexOf(e.dataset.id), 1);
    }
    
}


function sendDeleteRequest() {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'No, cancel!',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            
            $.ajax({
                method: "GET",
                url: "/api/deleteMember/",
                data: { "arr[]": delete_array },
                success: function (data) {
                    console.log("success on delete"+data);
                    update_table(data)
                },
                error: function() {
                    console.log('error');
                  }

            })
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelled',
                'Your imaginary file is safe :)',
                'error'
            )
        }
    })


}

function reloadPage() {
    window.location.reload();
    console.log("reload");
};





function resultperpageValueChanged(){
    let resultperpage = document.getElementById('resultperpage').value;
    let searchbytype=document.getElementById('searchbytype').value;
   
        $.ajax({
            method: "GET",
            url: "/api/searchbydata/",
            data: { "resultperpage": resultperpage, "searchbytype": searchbytype  },
            success: function (data) {
                console.log("success on search");
                console.log(data);
                update_table(data)
            
            },
            error: function () {
                console.log("error on get search by data");
            }
        });
    
    
};

function searchClick(){
    let fromdate = document.getElementById('fromdate').value;
    let todate = document.getElementById('todate').value;
    console.log(fromdate);
    console.log(todate);
    if (fromdate != "" && todate != ""){
        $.ajax({
            method: "GET",
            url: "/api/searchbydate/",
            data: { "fromdate": fromdate, "todate": todate },
            success: function (data) {
                console.log("success on search");
                console.log(data);
                update_table(data)
            
            },
            error: function () {
                console.log("error on get search by date");
            }
        });
    }

};

function searchbymembername(){
    let searchbyname = document.getElementById('searchbyname').value;
    console.log(searchbyname);
    $.ajax({
        method: "GET",
        url: "/api/searchbyname/",
        data: { "searchbyname": searchbyname },
        success: function (data) {
            console.log("success on search");
            console.log(data);
            update_table(data)
        
        },
        error: function () {
            console.log("error on get search by name");
        }
    });



};




function update_table(data) {
    console.log(data);
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        console.log(elem['member_name']);
        row =

            '<tr class="border-2 hover:bg-slate-300">' +
                '<td class="p-2">' +
                    '<input onclick="requestDelete(this)" data-id="' + elem['id'] +'" type="checkbox" class="cursor-pointer rounded-md" onc>' +
                '</td>' +
                '<td class="p-2">'+ elem['id'] +'</td>'+
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
                    '<span class="px-2 py-1 font-semibold leading-tight text-orange-700 bg-orange-100 rounded-full">'+ elem['active_fee_id']['status']+ '</span>'+
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
                    '<button x-on:click="openSMSModel();"'+
                        'class="bg-red-400 drop-shadow-md px-5 rounded-lg rounded-br-none">SMS</button>'+
                '</td>'+
            '</tr>';

        all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
}
