function addJson(headers, visible) {
    json_list = []
    for (i=0; i<headers.length; i++) {
        json_list.push({target: i, visible: visible[headers[i]], searchable: true, })
        //console.log(headers[i] + " : " + visible[headers[i]])
    }
    return json_list
}

function Delete_table() {
    console.log('delete_table')
    $('#pub_list').DataTable().destroy();
    $("#pub_list").remove();

}

function Search(headers, visible, order) {
    console.log('Search')
    //console.log(headers)
    //console.log(visible)
    //console.log(order)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: true,
            pagingType: 'first_last_numbers',
            info: false,
            //order: [[order, 'asc']],
            order: [[order, 'desc']],
            columnDefs: addJson(headers, visible)
        });
    });
}



function Reset() {
     window.location = "/pub/list";
}