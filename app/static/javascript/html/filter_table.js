function addJson(headers, visible) {
    json_list = []
    for (i=0; i<headers.length; i++) {
        json_list.push({target: i, visible: visible[headers[i]], searchable: true, })
        //console.log(headers[i] + " : " + visible[headers[i]])
    }
    return json_list
}

function Search(headers, visible) {
    console.log('inside Search')
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: true,
            info: false,
            order: [[9, 'desc']],
            columnDefs: addJson(headers, visible)
        });
    });
}

function SearchDay(headers, visible) {
    console.log('inside SearchDay')
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: true,
            info: false,
            columnDefs: addJson(headers, visible)
        });
    });
}

function Reset() {
     window.location = "/pub/list";
}