function addJson(headers, visible) {
    json_list = []
    for (i=0; i<headers.length; i++) {
        json_list.push({target: i, visible: visible[headers[i]], searchable: true, })
        //console.log(headers[i] + " : " + visible[headers[i]])
    }
    return json_list
}

function Search(headers, visible, order) {
    console.log('inside Search')
    console.log(headers)
    console.log(visible)
    console.log(order)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: true,
            info: false,
            order: [[48, 'asc']],
            columnDefs: addJson(headers, visible)
        });
    });
}



function Reset() {
     window.location = "/pub/list";
}