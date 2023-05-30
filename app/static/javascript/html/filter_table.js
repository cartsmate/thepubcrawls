function Search() {
    console.log('inside Search')
    document.getElementById("table-pubs-json").innerHTML = create_table()
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: false,
            info: false,
            order: [[8, 'desc']],
            columnDefs: [
                    {target: 0, visible: false, searchable: false, },
                    {target: 1, visible: true, searchable: true, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: true, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: false, searchable: false, },
                    {target: 7, visible: false, searchable: false, },
                    {target: 8, visible: true, searchable: true, },
                    {target: 9, visible: false, searchable: false, },
                    {target: 10, visible: false, searchable: false, },
                    {target: 11, visible: false, searchable: false, },
                    {target: 12, visible: false, searchable: false, },
                    {target: 13, visible: false, searchable: false, },
                    {target: 14, visible: false, searchable: false, },
                    {target: 15, visible: false, searchable: false, },
                    {target: 16, visible: false, searchable: false, },
                    {target: 17, visible: true, searchable: false, },
                    {target: 18, visible: true, searchable: false, }
                        ]
        });
    });
}

function Area() {
    console.log('inside Area')
    document.getElementById("table-pubs-json").innerHTML = create_table()
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: false,
            info: false,
            order: [[8, 'desc']],
            searching: false,
            columnDefs: [
                    {target: 0, visible: false, searchable: false, },
                    {target: 1, visible: true, searchable: true, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: false, searchable: false, },
                    {target: 7, visible: false, searchable: false, },
                    {target: 8, visible: true, searchable: true, },
                    {target: 9, visible: false, searchable: false, },
                    {target: 10, visible: false, searchable: false, },
                    {target: 11, visible: false, searchable: false, },
                    {target: 12, visible: false, searchable: false, },
                    {target: 13, visible: false, searchable: false, },
                    {target: 14, visible: false, searchable: false, },
                    {target: 15, visible: false, searchable: false, },
                    {target: 16, visible: false, searchable: false, },
                    {target: 17, visible: true, searchable: false, },
                    {target: 18, visible: true, searchable: false, }
                        ]
        });
    });
}

function Station() {
    console.log('inside Station')
    document.getElementById("table-pubs-json").innerHTML = create_table()
    $(document).ready(function () {
        $('#pub_list').DataTable({
            order: [[5, 'desc']],
            columnDefs: [
                    {target: 0, visible: true, searchable: true, },
                    {target: 1, visible: true, searchable: true, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: false, searchable: false, },
                    {target: 7, visible: false, searchable: false, },
                    {target: 8, visible: true, searchable: true, },
                    {target: 9, visible: false, searchable: false, },
                    {target: 10, visible: false, searchable: false, },
                    {target: 11, visible: false, searchable: false, },
                    {target: 12, visible: false, searchable: false, },
                    {target: 13, visible: false, searchable: false, },
                    {target: 14, visible: false, searchable: false, },
                    {target: 15, visible: false, searchable: false, },
                    {target: 16, visible: false, searchable: false, },
                    {target: 17, visible: true, searchable: false, },
                    {target: 18, visible: true, searchable: false, }
                        ]
        });
    });
}

function Category() {
    console.log('inside Category')
    document.getElementById("table-pubs-json").innerHTML = create_table()
    $(document).ready(function () {
        $('#pub_list').DataTable({
            paging: false,
            info: false,
            order: [[7, 'desc']],
            columnDefs: [
                    {target: 0, visible: true, searchable: true, },
                    {target: 1, visible: true, searchable: true, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: false, searchable: false, },
                    {target: 7, visible: false, searchable: false, },
                    {target: 8, visible: true, searchable: true, },
                    {target: 9, visible: false, searchable: false, },
                    {target: 10, visible: false, searchable: false, },
                    {target: 11, visible: false, searchable: false, },
                    {target: 12, visible: false, searchable: false, },
                    {target: 13, visible: false, searchable: false, },
                    {target: 14, visible: false, searchable: false, },
                    {target: 15, visible: false, searchable: false, },
                    {target: 16, visible: false, searchable: false, },
                    {target: 17, visible: true, searchable: false, },
                    {target: 18, visible: true, searchable: false, }
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