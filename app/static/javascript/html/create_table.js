function filter_table(mouse) {
    document.getElementById("table-pubs-json").innerHTML = '<p>' + mouse + '</p>'
}

function camel_case(word) {
    return String(word['0']).toUpperCase() + String(word).substring(1)
}
function create_table(filter, data) {
    console.log("create list of pubs")
    table_string = '<table id="pub_list" class="table table-striped">'
    table_string += '<thead><tr>' +
                        '<th>Name</th>' +
                        '<th>Category</th>' +
                        '<th>Station</th>' +
                        '<th>Area</th>' +
                        '<th>Star Quality</th>' +
                        '<th>Rev.</th>' +
                        '<th>Score</th>' +
                        '</tr></thead>'
   for (var key in pubs_reviews) {
        if (pubs_reviews[key].star == 0) {
            str_reviewed =
             '<td>None</a></td>' +
             '<td>None</a></td>'
        } else {
            str_reviewed =
            '<td><a href="/pub/star/' + pubs_reviews[key].star + '">' + camel_case(pubs_reviews[key].star) +'</a></td>' +
            '<td><a href="../review/' + pubs_reviews[key].pub_identity + '">Review</a></td>'
        }
        table_string += '<tr>' +
            '<td><a href="/pub/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].name + '</a></td>' +
            '<td><a href="/pub/category/' + pubs_reviews[key].category + '">' + camel_case(pubs_reviews[key].category) + '</a></td>' +
            '<td><a href="/pub/list/station/' + pubs_reviews[key].station + '">' + pubs_reviews[key].station + '</a></td>' +
            '<td><a href="/pub/list/area/' + pubs_reviews[key].area + '">' + pubs_reviews[key].area + '</a></td>' +
            str_reviewed +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].score + '</a></td>' +
            '</tr>'
    }
    table_string += '</table>'
    return table_string;
}
