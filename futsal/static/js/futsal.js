var delete_array = [];

function requestDelete(e) {
    
    if (e.checked) {
        delete_array.push(parseInt(e.dataset.id));
    } else {
        delete_array.splice(delete_array.indexOf(e.dataset.id), 1);
    }
    console.log(delete_array);

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
                url: "/api/deleteTeamRecord/",
                data: { "arr[]": delete_array },
                success: function (data) {
                    console.log("success on delete" + data);
                    update_table(data)
                },
                error: function () {
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





function SearchByFields() {
    let field = document.getElementById('search-by-field').value;
    let value = document.getElementById('search-by-value').value;
    console.log(field, value);
    if (field != '' && value != '') {
        $.ajax({
            method: "GET",
            url: "/api/SearchByFutsalField/",
            data: { "field": field, "value": value },
            success: function (data) {
                console.log("success on search" + data);
                update_table(data)
            },
            error: function () {
                console.log('error');
            }

        })
    }
};

// function searchClick(){
//     let fromdate = document.getElementById('fromdate').value;
//     let todate = document.getElementById('todate').value;
//     console.log(fromdate);
//     console.log(todate);
//     if (fromdate != "" && todate != ""){
//         $.ajax({
//             method: "GET",
//             url: "/api/searchByExpenseDate/",
//             data: { "fromdate": fromdate, "todate": todate },
//             success: function (data) {
//                 console.log("success on search");
//                 console.log(data);
//                 update_table(data)

//             },
//             error: function () {
//                 console.log("error on get search by date");
//             }
//         });
//     }

// };

// function searchbymembername(){
//     let searchbyname = document.getElementById('searchbyname').value;
//     console.log(searchbyname);
//     $.ajax({
//         method: "GET",
//         url: "/api/searchByExpenseHeadOfAccount/",
//         data: { "searchbyname": searchbyname },
//         success: function (data) {
//             console.log("success on search");
//             console.log(data);
//             update_table(data)

//         },
//         error: function () {
//             console.log("error on get search by name");
//         }
//     });



// };




function update_table(data) {
    console.log(data);
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        console.log(elem['id']);
        row =

        '<tr class="border-2 hover:bg-slate-300">'+
        '<td class="p-1">'+
            '<input onclick="requestDelete(this)" data-id="' + elem['id'] +'" type="checkbox" class="cursor-pointer rounded-md" >' +
        '</td>'+
        '<td class="p-1">'+elem['id']+'</td>'+
        '<td class="p-1">'+elem['member_created_at']+'</td>'+
        '<td class="p-1">'+elem['team_name']+'</td>'+
        '<td class="p-1">'+elem['captain_name']+'</td>'+
        '<td class="p-1">'+elem['contact_number']+'</td>'+
        '<td class="p-1">'+elem['team_attended_by']+'</td>'+

        '<td class="p-1">'+
            '<a href="/futsalMatch/?futsal-match='+elem['id']+'">'+
                '<button'+
                'class="bg-green-600 drop-shadow-md px-1 py-1 rounded-lg inline-flex items-center rounded-br-none">'+
                '<span>Match</span>'+
                '<svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5"'+
                    'viewBox="0 0 20 20" fill="currentColor">'+
                    '<path fill-rule="evenodd"'+
                        'd="M12 1.586l-4 4v12.828l4-4V1.586zM3.707 3.293A1 1 0 002 4v10a1 1 0 00.293.707L6 18.414V5.586L3.707 3.293zM17.707 5.293L14 1.586v12.828l2.293 2.293A1 1 0 0018 16V6a1 1 0 00-.293-.707z"'+
                        'clip-rule="evenodd" />'+
                '</svg>'+
                '</button>'+
            '</a>'+
            '<a href="/teamDetails/?team-details='+ elem['id'] +'">'+
                '<button '+
                'class="bg-blue-600 drop-shadow-md px-1 py-1 rounded-lg inline-flex items-center rounded-br-none">'+
                                                '<span>Edit</span>'+
                                                '<svg xmlns="http://www.w3.org/2000/svg" class="h-4 ml-2 w-4" fill="none"'+
                                                    'viewBox="0 0 24 24" stroke="currentColor">'+
                                                    '<path stroke-linecap="round" stroke-linejoin="round"'+
                                                        'stroke-width="2"'
                                                       ' d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />'+
                                                '</svg>'+
                '</button>'+
            '</a>'+

        '</td>'+
    '</tr>' 

    

        all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
}
