function Area() {
    console.log('inside Area')
    document.getElementById("table-pubs-json").innerHTML = create_table(pubs_reviews)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: false,
            info: false,
            order: [[7, 'desc']],
            columnDefs: [
                    {target: 0, visible: true, searchable: true, },
                    {target: 1, visible: true, searchable: false, },
                    {target: 2, visible: true, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: true, searchable: true, },
                    {target: 7, visible: true, searchable: true, }
                        ]
        });
    });
}

function Station() {
    console.log('inside Station')
    document.getElementById("table-pubs-json").innerHTML = create_table(pubs_reviews)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            order: [[5, 'desc']],
            columnDefs: [
                    {target: 1, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                        ]
        });
    });
}

function Category() {
    console.log('inside Category')
    document.getElementById("table-pubs-json").innerHTML = create_table(pubs_reviews)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            order: [[5, 'desc']],
            columnDefs: [
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                        ]
        });
    });
}

function Star() {
    document.getElementById("table-pubs-json").innerHTML = create_table(pubs_reviews)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            order: [[5, 'desc']],
            columnDefs: [
                    {target: 1, visible: false, searchable: false, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                        ]
        });
    });
}

function Reset() {
     window.location = "/pub/list";
}