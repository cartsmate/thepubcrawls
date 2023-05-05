function Search() {
    console.log('inside Search')
    document.getElementById("table-pubs-json2").innerHTML = create_table2()
    $(document).ready(function () {
        $('#pub_list2').DataTable({
            paging: false,
            info: false,
            order: [[7, 'desc']],
            columnDefs: [
                    {target: 0, visible: true, searchable: true, },
                    {target: 1, visible: false, searchable: false, },
                    {target: 2, visible: false, searchable: false, },
                    {target: 3, visible: false, searchable: false, },
                    {target: 4, visible: false, searchable: false, },
                    {target: 5, visible: false, searchable: false, },
                    {target: 6, visible: false, searchable: false, },
                    {target: 7, visible: true, searchable: true, },
                    {target: 8, visible: false, searchable: false, },
                    {target: 9, visible: false, searchable: false, },
                    {target: 10, visible: false, searchable: false, },
                    {target: 11, visible: false, searchable: false, },
                    {target: 12, visible: false, searchable: false, },
                    {target: 13, visible: false, searchable: false, },
                    {target: 14, visible: false, searchable: false, },
                    {target: 15, visible: false, searchable: false, },
                    {target: 16, visible: true, searchable: false, },
                    {target: 17, visible: true, searchable: false, }
                        ]
        });
    });
}
