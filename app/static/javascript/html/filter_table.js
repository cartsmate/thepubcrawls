function addJson(headers, visible) {
    json_list = []
    for (i=0; i<headers.length; i++) {
        json_list.push({target: i, visible: visible[headers[i]], searchable: true, })
        //console.log(headers[i] + " : " + visible[headers[i]])
    }
    console.log('json_list')
    console.log(json_list)
    return json_list
}

function delete_table() {
    console.log('delete_table')
    $('#pub_list').DataTable().destroy();
    $("#pub_list").remove();

}

function filter_table(visible, order, asc_desc) {
    console.log('FILTER_TABLE')
    //console.log('headers')
    //console.log(headers)
    //console.log('pre-visible')
    //console.log(visible)
    for (const key in visible) {
        let trueStr = visible[key]
        //console.log(typeof(trueStr) + " : " + trueStr)
        trueStr = (trueStr === "true")
        //console.log(typeof(trueStr) + " : " + trueStr)
        visible[key] = trueStr
    }
    //console.log('post-visible')
    //console.log(visible)
    //console.log('order')
    //console.log(order)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: true,
            //pagingType: 'first_last_numbers',
            info: false,
            //order: [[order, 'asc']],
            order: [[order, asc_desc]],
            columnDefs: addJson(headers, visible)
        });
    });
    //console.log('end of filter table')
}


function Reset() {
     window.location = "/pub/list";
}