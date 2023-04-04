function displayNone(pub) {
    table_string = '<table id="pub_list" class="table table-striped">'
    table_string += '<thead><tr>' +
                        '<th>Stop</th>' +
                        '<th>Name</th>' +
                        '<th>crawl.favourite</th>' +
                        '<th>Walk</th>' +
                    '</tr></thead>'
    table_string += '<tr>' +
        '<td>A</td>' +
        '<td>' + pub[0]['name'] + '</td>' +
        '<td>' + pub[0]['score'] + '%</td>' +
        '<td></td>' +
                    '</tr>'
    table_string += '<tr>' +
        '<td>-</td>' +
        '<td>No pub crawls fit that criteria</td>' +
        '<td></td>' +
        '<td></td>' +
                    '</tr>'
    table_string += '</table>'
    document.getElementById('route').innerHTML = table_string
}
