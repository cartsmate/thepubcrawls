function Area() {
    document.getElementById("table-pubs-json").innerHTML = create_table(pubs_reviews)
    $(document).ready(function () {
        $('#pub_list').DataTable({
            order: [[5, 'desc']],
            columnDefs: [
                    {target: 1, visible: false, searchable: false, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                        ]
        });
    });
}

function Station() {
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